import logging
import re

from vkbottle.bot import rules

log = logging.getLogger(__name__)


class SearaCommandRule(rules.ABCMessageRule):
    def __init__(self, commands, invert=False):
        self.commands = commands
        self.invert = invert
        log.info(f"SearaCommandRule inited with invert {invert}")

    async def check(self, message):
        for key, value in self.commands.items():
            match = re.match(key, message.text)
            if match:
                log.info(f"Match {key}")
                if self.invert is True:
                    return False
                else:
                    return {"command": value}
        return bool(self.invert - False)


class SearaFromFriendsRule(rules.ABCMessageRule):
    def __init__(self, friends):
        self.friends = friends
        log.info("SearaFromFriendsRule inited")

    async def check(self, message):
        log.info(f"Message from friend = {message.from_id in self.friends}")
        return message.from_id in self.friends


class SearaRoflRule(rules.ABCMessageRule):
    def __init__(self, rofls, invert=False):
        self.rofls = rofls
        self.invert = invert
        log.info(f"SearaRoflRule inited with invert {invert}")

    async def check(self, message):
        for key, value in self.rofls.items():
            match = re.match(key, message.text)
            if match:
                log.info(f"Match {key}")
                if self.invert is True:
                    return False
                else:
                    return {"rofl": key}
        return bool(self.invert - False)
