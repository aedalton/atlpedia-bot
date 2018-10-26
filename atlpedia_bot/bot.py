import datetime


class AtlpediaBot(object):
    def __init__(self, channel_name="#atlantopedia"):
        self.channel_name = channel_name
        self.client = None
        pass

    def ping_hosts(self):
        # ping the hosts every 3rd Tuesday of the month to get a welcome
        # message and kick off the event; if no response, use default
        welcome_response = sc.api_call(
            "chat.postMessage",
            channel="#atlantopedia-hosts",
            text="Hello from Atlantopedia-Bot! :tada: It's time to schedule
            this month's event. Would you like to customize the message or
            use the default?",
            reply_broadcast=True
        )
        welcome_response.get("ts")
        

    @classmethod
    def recruit_volunteers(cls, a, b):
        self.client.api_call(
            "chat.postMessage",
            channel=self.channel_name,
            text=None
        )
        print(str(a) + ' ' + str(b))

    @classmethod
    def schedule_event(self):
        pass

    def update_channel_topic(self):
        # channels.setTopic
        pass

    
        
