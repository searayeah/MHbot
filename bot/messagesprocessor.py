import json
import logging
import random
from io import BytesIO
from vkbottle import PhotoMessageUploader

log = logging.getLogger(__name__)


class MessagesProcessor:
    def __init__(self, data, base, bot_api):
        self.data = data
        self.base = base
        self.bot_api = bot_api
        log.info("MessagesProcessor inited")

    async def get_data_from_link(self, link) -> BytesIO:
        async with self.bot_api.http as session:
            return BytesIO(await session.request_content("GET", link))

    def reply(self, message):
        return json.dumps(
            {
                "is_reply": 1,
                "peer_id": message.peer_id,
                "conversation_message_ids": [message.conversation_message_id],
            }
        )

    def poop_meme_answer(self, counter, type_):
        if counter == 0:
            return {"message": self.data["nothing_added"]}
        else:
            return {
                "message": self.data["added_counter_sth"].format(
                    counter=counter, sth=type_
                )
            }

    def gather_attachments(self, message):
        attachment_list = message.attachments
        if message.fwd_messages:
            for message in message.fwd_messages:
                log.info(f"Searching in fwd_messages")
                attachment_list.extend(self.gather_attachments(message))
        if message.reply_message:
            log.info(f"Searching in reply_message")
            attachment_list.extend(self.gather_attachments(message.reply_message))
        log.info(f"Executed gather_attachments")
        return attachment_list

    async def process_command(self, command, message):
        if command == "/+poop":
            counter = 0
            poops = self.gather_attachments(message)
            for poop in poops:
                if poop.video:
                    video_code = (
                        "video" + str(poop.video.owner_id) + "_" + str(poop.video.id)
                    )
                    log.info(f"Entered /+poop command, sending {video_code}")
                    if self.base.post_poop(video_code, poop.video.title):
                        counter += 1
            return self.poop_meme_answer(counter, "пуп")

        elif command == "/+meme":
            counter = 0
            memes = self.gather_attachments(message)
            for meme in memes:
                if meme.photo:
                    photo_link = meme.photo.sizes[-1].url
                    log.info(f"Entered /+meme command, sending {photo_link}")
                    if self.base.post_meme(photo_link):
                        counter += 1

            return self.poop_meme_answer(counter, "мем")

        elif command == "/poop":
            poop_to_post = random.choice(self.base.get_values("poops"))
            log.info(f"Entered /poop command, returning poop {poop_to_post}")
            return {"attachment": poop_to_post}

        elif command == "/meme":
            meme_to_post = random.choice(self.base.get_values("memes"))
            log.info(f"Entered /meme command, returning meme {meme_to_post}")
            meme_link = await self.get_data_from_link(meme_to_post)
            meme_as_attachment = await PhotoMessageUploader(
                self.bot_api, generate_attachment_strings=True
            ).upload(meme_link)
            return {"attachment": meme_as_attachment}

        elif command == "/help":
            log.info("Entered /help command")
            return {"message": "\n".join(self.data["help_reply"])}

        elif command == "/github":
            log.info("Entered /github command")
            return {"message": self.data["github_link"]}

    def process_rofl(self, rofl, message):
        log.info(f"Entered process_rofl {rofl}")
        if type(self.data["rofls"][rofl]) is dict:
            return self.data["rofls"][rofl]
        elif type(self.data["rofls"][rofl]) is list:
            return {"message": random.choice(self.data["rofls"][rofl])}
        else:
            return {"message": self.data["rofls"][rofl]}

    def process_forwarded_message(self):
        log.info("Entered process_forwarded_message")
        return random.choice(self.data["forward_reply"])

    def process_random_message(self, names, message):
        name = random.choice(names)
        answer = random.choice(self.base.get_values(name))
        log.info(f"Entered process_random_message, returning {answer} from {name}")
        return answer
