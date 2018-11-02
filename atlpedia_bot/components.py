# -*- coding: utf-8 -*-
"""
Slack Interactive/Message Components
"""

MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

MONTH_OPTIONS = [{"label": MONTHS[x], "value": x + 1} for x in range(len(MONTHS))]

# str(day).zfill(2)
DAY_OPTIONS = [{"label": str(day), "value": day} for day in range(1, 32)]


EVENT_VOLUNTEER_DIALOG = {
    "callback_id": "talk-46e2b0",  #  An identifier strictly for you to recognize submissions of this particular instance of a dialog
    "title": "Tell us about your talk!",
    "submit_label": "Schedule",
    "notify_on_cancel": True,
    "state": "talk_submission", # An optional string that will be echoed back to your app when a user interacts with your dialog
    "elements": [
        {
            "type": "text",
            "label": "Title",
            "name": "talk_title",
        },
        {
            "type": "textarea",
            "label": "Description",
            "name": "talk_description",
        },
        {
            "type": "select",
            "label": "Powerpoint or visuals?",
            "name": "talk_visuals",
            "options": [
                {
                    "label": "Yes",
                    "value": "yes"
                },
                {
                    "label": "No",
                    "value": "no"
                },
            ]
        },        
    ]
}

RECRUIT_VOLUNTEERS_MESSAGE = [
    {
        "text": "Would you like to volunteer at the next Atlantopedia?",
        "fallback": "Sorry! I am unable to volunteer you at this time.",
        "callback_id": "schedule_button",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "actions": [
            {
                "name": "option",
                "text": "Yes! DM me.",
                "type": "button",
                "value": "yes"
            },
            {
                "name": "option",
                "text": "Ask me tomorrow!",
                "style": "warning",
                "type": "button",
                "value": "later"
            }
        ]
    }
]

EVENT_SCHEDULE_DIALOG = {
    "callback_id": "event-46e2b0",
    "title": "New Atlantopedia Event",
    "submit_label": "Schedule",
    "notify_on_cancel": True,
    "state": "event_date",
    "elements": [
        {
            "type": "select",
            "label": "Month",
            "name": "event_month",
            "options": MONTH_OPTIONS
        },
        {
            "type": "select",
            "label": "Day",
            "name": "event_day",
            "options": DAY_OPTIONS
        },
        {
            "type": "select",
            "label": "Year",
            "name": "event_year",
            "options": [
                {
                    "label": "2018",
                    "value": 2018
                },
                {
                    "label": "2019",
                    "value": 2019
                }
            ]
        }
    ]
}

SCHEDULE_REMINDER_MESSAGE = [
    {
        "text": "Should we message the channel about the next Atlantopedia?",
        "fallback": "You are unable to schedule at this time",
        "callback_id": "schedule_button",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "actions": [
            {
                "name": "option",
                "text": "Yes! Let's build the message now.",
                "type": "button",
                "value": "yes"
            },
            {
                "name": "option",
                "text": "No. Try again later.",
                "style": "danger",
                "type": "button",
                "value": "no",
                "confirm": {
                    "title": "Are you sure?",
                    "text": "Wouldn't you prefer to get this out of the way?",
                    "ok_text": "Fine.",
                    "dismiss_text": "No, go away."
                }
            }
        ]
    }
]
