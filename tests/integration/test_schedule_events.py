import os

import pytest


@pytest.fixture
def dialog_submission_1():
    return {
        "type": "dialog_submission",
        "submission": {
            "name": "Sigourney Dreamweaver",
            "email": "sigdre@example.com",
            "phone": "+1 800-555-1212",
            "meal": "burrito",
            "comment": "No sour cream please",
            "team_channel": "C0LFFBKPB",
            "who_should_sing": "U0MJRG1AL"
        },
        "callback_id": "employee_offsite_1138b",
        "state": "vegetarian",
        "team": {
            "id": "T1ABCD2E12",
            "domain": "coverbands"
        },
        "user": {
            "id": "W12A3BCDEF",
            "name": "dreamweaver"
        },
        "channel": {
            "id": "C1AB2C3DE",
            "name": "coverthon-1999"
        },
        "action_ts": "936893340.702759",
        "token": os.environ.get("SLACK_TOKEN"),
        "response_url": ""  # TBD
    }
