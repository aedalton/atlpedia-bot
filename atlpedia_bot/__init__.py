import flask
import json
import time

from apscheduler.schedulers.background import BackgroundScheduler

from atlpedia_bot.routes import event_views
from atlpedia_bot import bot


def create_app():
    app = flask.Flask(__name__)
    app.register_blueprint(event_views)

    return app
