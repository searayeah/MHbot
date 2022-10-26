import logging
import gspread

log = logging.getLogger(__name__)


class GoogleBase:
    def __init__(
        self, token, sheet_key, sheet_poop_name, sheet_meme_name, sheet_names_names
    ):
        self.token = token
        self.sheet_key = sheet_key
        self.sheet_poop_name = sheet_poop_name
        self.sheet_meme_name = sheet_meme_name
        self.sheet_names_names = sheet_names_names

        self.sheet_poop = self._get_sheet(self.sheet_poop_name)
        self.sheet_meme = self._get_sheet(self.sheet_meme_name)
        self.sheet_names = {x: self._get_sheet(x) for x in self.sheet_names_names}
        log.info(
            f"GoogleBase inited with poop sheet {sheet_poop_name}, "
            + f"meme sheet {sheet_meme_name} and names {sheet_names_names}"
        )

    def _get_sheet(self, sheet_name):
        gc = gspread.service_account_from_dict(self.token)
        sh = gc.open_by_key(self.sheet_key)
        return sh.worksheet(sheet_name)

    def get_values(self, sheet_name):
        if sheet_name == "poops":
            return self.sheet_poop.col_values(1)
        elif sheet_name == "memes":
            return self.sheet_meme.col_values(1)
        else:
            return self.sheet_names[sheet_name].col_values(1)

    def post_poop(self, video, title):
        poops = self.get_values("poops")
        if video in poops:
            log.info(f"Poop {video} is already present in GoogleBase")
            return False
        else:
            self.sheet_poop.append_row(
                [video, f'=HYPERLINK("https://vk.com/{video}", "{title}")'],
                value_input_option="USER_ENTERED",
            )
            log.info(f"Poop {video} has been added to GoogleBase")
            return True

    def post_meme(self, meme):
        memes = self.get_values("memes")
        if meme in memes:
            log.info(f"Meme {meme} is already present in GoogleBase")
            return False
        else:
            self.sheet_meme.append_row(
                [meme, f'=IMAGE("{meme}")'],
                value_input_option="USER_ENTERED",
            )
            log.info(f"Meme {meme} has been added to GoogleBase")
            return True

    def post_message(self, name, message):
        self.sheet_names[name].append_row([message])
        log.info(f"Single message {message} was sent to GoogleBase")

    def post_messages(self, name, messages):
        self.sheet_names[name].append_rows(messages)
        log.info(f"Multiple messages {messages} were sent to GoogleBase")

    # Unused
    def _refresh_poops(self):
        """
        Clears worksheet
        Deletes duplicates
        """
        whole_sheet = self.sheet_poop.get_all_values()
        good_poops = dict(whole_sheet)
        self.sheet_poop.resize(1)
        self.sheet_poop.clear()
        self.sheet_poop.append_rows(list(good_poops.items()))
        log.info("Poops collection has been refreshed")
