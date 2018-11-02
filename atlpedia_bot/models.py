import os
import datetime

import peewee as pw
import playhouse.postgres_ext as playhouse
from playhouse.db_url import connect


db = connect(os.environ.get('DATABASE_URI', None))


class BaseModel(pw.Model):
    # NB: peewee will automatically add an auto-incrementing integer
    # primary key field named id
    class Meta:
        database = db

    created_at = pw.DateTimeField(default=datetime.datetime.now)
    updated_at = pw.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super().save(*args, **kwargs)


class User(BaseModel):
    username = pw.CharField(unique=True)
    slack_id = pw.CharField(unique=True)


class Submission(BaseModel):  # talk submissions
    user = pw.ForeignKeyField(User, backref='submissions')
    title = pw.CharField()
    description = pw.TextField()
    selected = pw.BooleanField(default=False)


class Event(BaseModel):  # make a new event each time
    scheduled_date = pw.DateTimeField(unique=True)
    welcome_message = pw.TextField(null=True)
    description = pw.TextField(null=True)
    submissions = pw.ForeignKeyField(Submission, backref="event", null=True)
    is_active = pw.BooleanField(default=False)


def init_db():
    with db:
        db.drop_tables([User, Submission, Event], safe=True)
        db.create_tables([User, Submission, Event])
