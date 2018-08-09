from rtmbot import RtmBot
from rtmbot.core import Plugin

import secret
import chatlogic

class HelloPlugin(Plugin):
    def process_message(self, data):
        reply = answer(data["text"])
        if reply is not none:
            self.outputs.append([data["channel"], reply])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
