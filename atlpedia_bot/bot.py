import datetime
import json
import os

import atexit
import flask
from slackclient import SlackClient

from atlpedia_bot import components


class AtlpediaScheduler(object):
    def __init__(self, app=None):
        self.scheduler = BackgroundScheduler()
        atexit.register(lambda: self.scheduler.shutdown())

    def init(self):
        self.scheduler.add_job(func=self.ping_hosts, trigger="interval", seconds=10)
        self.scheduler.start()

    def ping_hosts(self):
        # ping the hosts every 3rd Tuesday of the month to get a welcome
        # message and kick off the event; if no response, use default
        pass

    @classmethod
    def recruit_volunteers(cls):
        return cls.ping_channel(components.RECRUIT_VOLUNTEERS_MESSAGE)


    @classmethod
    def send_volunteer_dialog(cls, payload):
        dialog_response = cls.client.api_call("dialog.open",                                       
                                              trigger_id=payload.get("trigger_id"),
                                              dialog=components.VOLUNTEER_DIALOG)
        print(dialog_response)
        return dialog_response

    @classmethod
    def complete_volunteer_signup(cls, payload):
        complete_response = cls.client.api_call("chat.postMessage",
                                                channel=cls.channel,
                                                text="all done! follow up soon.",
                                                reply_broadcast=False,
                                                response_url=payload.get("response_url"))
        # do signing up here
        return

    @classmethod
    def ping_channel(cls, message, broadcast=False):
        message_attachment = json.dumps(message)

        # if (Events.volunteers):
        return cls.client.api_call("chat.postMessage",
                                   channel=cls.channel,
                                   reply_broadcast=broadcast,
                                   attachments=message_attachment)

    @classmethod
    def open_create_event_dialog(cls, trigger_id):
        response = cls.client.api_call("dialog.open",
                                       trigger_id=trigger_id,
                                       dialog=components.SCHEDULE_DIALOG)
        return response

    @classmethod
    def create_event_from_dialog(cls, original_dialog):
        submission = original_dialog.get("submission")

        # do event creation stuff here

        response = cls.client.api_call("chat.postMessage",
                                       channel=cls.channel,
                                       text="all done",
                                       reply_broadcast=False,
                                       response_url=original_dialog.get("response_url"))
        return

    # TODO: update channel topic
