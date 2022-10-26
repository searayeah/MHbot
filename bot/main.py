import logging
import os
import random

import yaml
from vkbottle.bot import Bot, rules

from googlebase import GoogleBase
from messagesprocessor import MessagesProcessor
from seararules import SearaCommandRule, SearaFromFriendsRule, SearaRoflRule


# Logging level can be set through .basicConfig(level=LOGGING_LEVEL)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

SHEET_KEY = os.environ["sheet_key"]
SHEET_POOP = "poops"
SHEET_MEME = "memes"
IDS_NAMES = {
    406826633: "andrei",
    204679786: "slava",
    113637897: "danya",
    380058716: "vova",
    482015078: "vanya",
}
TOKEN_NAMES_LIST = [
    "type",
    "project_id",
    "private_key_id",
    "private_key",
    "client_email",
    "client_id",
    "auth_uri",
    "token_uri",
    "auth_provider_x509_cert_url",
    "client_x509_cert_url",
]
TOKEN = {item: os.environ[item].replace("\\n", "\n") for item in TOKEN_NAMES_LIST}
VK_TOKEN = os.environ["vk_token"]

with open("bot/data/dictionary.yaml", "r") as stream:
    data = yaml.safe_load(stream)

bot = Bot(VK_TOKEN)
google_base = GoogleBase(TOKEN, SHEET_KEY, SHEET_POOP, SHEET_MEME, IDS_NAMES.values())
messages_processor = MessagesProcessor(data, google_base, bot.api)


@bot.on.message(
    SearaCommandRule(commands=data["commands"], invert=True),
    SearaRoflRule(rofls=data["rofls"], invert=True),
    SearaFromFriendsRule(IDS_NAMES.keys()),
    rules.MessageLengthRule(5),
)
async def main_handler(message, command=None, rofl=None):
    google_base.post_message(IDS_NAMES[message.from_id], message.text)
    log.info(f"message {message.text} saved")
    if random.randint(1, 100) == -5:
        await message.answer(
            messages_processor.process_random_message(
                list(IDS_NAMES.values()), message
            ),
            forward=messages_processor.reply(message),
        )
        log.info(f"main handler replied")


@bot.on.message(SearaCommandRule(commands=data["commands"]))
async def commands_handler(message, command):
    await message.answer(
        **await messages_processor.process_command(command, message),
        forward=messages_processor.reply(message),
    )
    log.info("command message handled")


@bot.on.message(SearaRoflRule(rofls=data["rofls"]))
async def rolfs_handler(message, rofl):
    if random.randint(1, 100) == -5:
        await message.answer(
            **messages_processor.process_rofl(rofl, message),
            forward=messages_processor.reply(message),
        )
        log.info("rofl message responsec")
    log.info("rofl message handled")


@bot.on.message((rules.ForwardMessagesRule(), rules.AttachmentTypeRule("wall")))
async def forward_message_handler(message):
    if random.randint(1, 100) == -5:
        await message.answer(
            messages_processor.process_forwarded_message(),
            forward=messages_processor.reply(message),
        )
        log.info("forward message responsed")
    log.info("forward message handled")


bot.run_forever()
