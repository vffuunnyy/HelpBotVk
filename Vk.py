import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

import Command
import Trigger

TOKEN = ""
BOT_ID = 283644170
ADMINS = [283644170]
PREFIX = "-->"

trigger = Trigger.Trigger()
command = Command.Command()

api = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(api)
vk = api.get_api()


@command.add(True)
def name(ev):
    print(ev.raw)


def parseMessage(ev):
    # trigger.handle(ev)
    # command.handle(ev)

    # event.attachments["attach1_kind"] == "audiomsg"
    pass


def send(peer, msg="", attachs=None):
    att = ""
    for attach in attachs: att.join(attach + ',')

    vk.messages.send(peer_id=peer, message=PREFIX + msg, attachment=att)


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_chat:
                parseMessage(event)
