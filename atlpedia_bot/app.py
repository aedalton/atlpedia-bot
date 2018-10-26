import atexit
import flask
import json
import time

from apscheduler.schedulers.background import BackgroundScheduler


app = flask.Flask(__name__)


def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=60)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

@app.route("/", methods=["GET"])
@app.route("/health", methods=["GET"])
def health():
    return flask.Response(json.dumps({"health": "okay"}), mimetype="application/json"), 200

@app.route("/events", methods=["POST"])
def events():
    if flask.request.data:
        data = json.loads(flask.request.data)
        return flask.Response(json.dumps({
            "token": data.get("token"),
            "challenge": data.get("challenge"),
        }), mimetype="application/json"), 200

    return flask.Response("error"), 400

if __name__ == "__main__":
    app.run()
