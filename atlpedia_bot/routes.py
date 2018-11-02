import json
import os
import datetime

import flask
from slackclient import SlackClient

from atlpedia_bot import components, models


event_views = flask.Blueprint('events', __name__)


CHANNEL = "CDQ8E1V8Q"
client = SlackClient(os.environ.get("SLACK_TOKEN"),
                     client_id=os.environ.get("SLACK_CLIENT_ID"),
                     client_secret=os.environ.get("SLACK_CLIENT_SECRET"))


@event_views.route("/", methods=["GET"])
@event_views.route("/health", methods=["GET"])
def health():
    return flask.Response(json.dumps({"health": "okay"}), mimetype="application/json"), 200


@event_views.route("/slash", methods=["GET", "POST"])
def slash_commands():
    if flask.request.form:
        command = flask.request.form.get('command')
        trigger_id = flask.request.form.get('trigger_id')
        text = flask.request.form.get('text')
        print(text)
        
        if 'schedule' in text:
            # open_create_event_dialog
            response = client.api_call("dialog.open",
                                       trigger_id=trigger_id,
                                       dialog=components.EVENT_SCHEDULE_DIALOG)
            print(response)
 
        if 'recruit' in text:
            # recruit_volunteers
            message_attachment = json.dumps(components.RECRUIT_VOLUNTEERS_MESSAGE)
            client.api_call("chat.postMessage",
                            channel=CHANNEL,
                            reply_broadcast=broadcast,
                            attachments=message_attachment)

        return flask.Response({}, status=200, mimetype='application/json')


@event_views.route("/events", methods=["GET", "POST"])
def events():
    # dispatcher
    if flask.request.form:
        command = flask.request.form.get('command')
        if command == '/test':
            return flask.Response(json.dumps({"status": "okay"}), status=200, mimetype='application/json')

        if flask.request.form.get('payload'):
            payload = json.loads(flask.request.form.get('payload'))
            user = payload.get("user")

            if payload.get("type") == "dialog_submission":
                submission = payload.get("submission")
                if payload.get("state") == "event_date":
                    # create_event_from_dialog
                    # do event creation stuff here
                    event_month = int(submission.get("event_month"))
                    event_day = int(submission.get("event_day"))
                    event_year = int(submission.get("event_year"))

                    event_datetime = datetime.datetime(year=event_year, month=event_month, day=event_day)

                    new_event = models.Event(scheduled_date=event_datetime,
                                             welcome_message=None,
                                             description=None)
                    new_event.save()
                    
                    # announce done creating event
                    response = client.api_call("chat.postMessage",
                                               channel=CHANNEL,
                                               text="all done",
                                               reply_broadcast=False,
                                               response_url=payload.get("response_url"))

                if payload.get("state") == "talk_submission":
                    user_model = models.User.get_or_none(slack_id=user.get("id"))
                    if not user_model:
                        user_model = models.User(slack_id=user.get("id"), username=user.get("name"))
                    user_model.save()

                    event_model = models.Event.select().where(Event.is_active == True).get()
                    submission_model = models.Submission(user=user_model,
                                                         title=submission.get("talk_title"),
                                                         description=submission.get("talk_description"))
                    submission_model.save()
                    if event_model:
                        event_model.submissions.add(submission_model)
                        event_model.save()
                    # complete_volunteer_signup
                    client.api_call("chat.postMessage",
                                    channel=CHANNEL,
                                    text="all done! follow up soon.",
                                    reply_broadcast=False,
                                    response_url=payload.get("response_url"))                    

            if payload.get("type") == "interactive_message":
                # send volunteer dialog
                client.api_call("dialog.open",
                                trigger_id=payload.get("trigger_id"),
                                dialog=components.EVENT_VOLUNTEER_DIALOG)

            return flask.Response({}, status=200, mimetype='application/json')

    return flask.Response("here"), 200
