# from vkbottle.bot import rules
# from string import punctuation
# from nltk.tokenize import word_tokenize
# from pymystem3 import Mystem
# from vkbottle.tools.dev_tools.mini_types.bot.message import MessageMin

# punctuation_chars = set(punctuation)
# mystem_analyzer = Mystem(entire_input=False)


# def MyTokenizer(sentence):
#     tokens = mystem_analyzer.lemmatize(sentence.lower())
#     tokens = [x for x in tokens if (len(set(x) & punctuation_chars) == 0)]
#     # return ' '.join(tokens)
#     return set(tokens)

# Message = MessageMin


# class SearaRule(rules.ABCMessageRule):

#     def __init__(self, pattern):
#         if isinstance(pattern, str):
#             self.pattern = [pattern]
#         else:
#             self.pattern = pattern

#     async def check(self, message: Message):
#         tokenized_message = MyTokenizer(message.text)
#         print(tokenized_message)
#         if len(set(self.pattern) & tokenized_message) != 0:
#             return True
#         else:
#             return False


# @bot.on.message(text=["/балабоба <item>", "/балабоба"])
# async def balaboba_handler(message: Message, item):
#     await message.answer('Не пашет нихуя ')
#     # if item is None:
#     #     item = random.choice(data_['persons']) + \
#     #         ' ' + random.choice(data_['verbs'])
#     # await message.answer(f'Загружаю запрос "{item}"...')
#     # try:
#     #     await message.answer(await generator(item))
#     # except Exception as e:
#     #     logging.error(e)
#     #     return "Сори, я на чилле 😉💨"

# @bot.on.message((rules.VBMLRule(['Да <item>', 'да <item>']),
#                  rules.RegexRule(['Да.*', 'да.*'])))
# async def yes(message: Message, item=None, *args, **kwargs):
#     r_number = random.randint(101)
#     if r_number < 20:
#         await message.answer('Нет.', forward=reply(message))
#     if 20 <= r_number < 40:
#         await message.answer('пизда', forward=reply(message))
#     if item is not None and 40 <= r_number < 80:
#         await message.answer(f'{item}...', forward=reply(message))

# @bot.on.message((rules.VBMLRule(['Нет <item>', 'нет <item>', 'не <item>', 'Не <item>',
#                                  'Да не', 'да не']),
#                  rules.RegexRule(['Не.*', 'не.*'])))
# async def no(message: Message, item=None, *args, **kwargs):
#     r_number = random.randint(101)
#     if r_number < 20:
#         await message.answer('Да.', forward=reply(message))
#     if item is not None and 40 <= r_number < 80:
#         await message.answer(f'{item}...', forward=reply(message))


# GET MESSAGES FROM CHAT ALL MESSAGES
# from vkbottle import API
# import asyncio
# import pandas as pd
# from googlebase import GoogleBase
# import os

# SHEET_KEY = ''
# SHEET_POOP = 'poops'
# IDS_NAMES = {406826633: 'andrei',
#              204679786: 'slava',
#              113637897: 'danya',
#              380058716: 'vova',
#              482015078: 'vanya'}
# TOKEN_NAMES_LIST = ["type",
#                     "project_id",
#                     "private_key_id",
#                     "private_key",
#                     "client_email",
#                     "client_id",
#                     "auth_uri",
#                     "token_uri",
#                     "auth_provider_x509_cert_url",
#                     "client_x509_cert_url"]
# TOKEN = {item: os.environ[item].replace(
#     '\\n', '\n') for item in TOKEN_NAMES_LIST}

# a = GoogleBase(TOKEN, SHEET_KEY, SHEET_POOP, IDS_NAMES.values())
# import time

# import vk_api

# vk_session = vk_api.VkApi(
#     token='')

# vk = vk_session.get_api()


# def main():
#     ID_LISTS = {406826633: [],
#                 204679786: [],
#                 113637897: [],
#                 380058716: [],
#                 482015078: []}
#     # resid = 5323
#     resid = 50649
#     offset = 0
#     while resid > 0:
#         messages_all = vk.messages.getHistory(
#             count=200, peer_id=2000000000 + x, offset=offset)
#         time.sleep(1)
#         resid -= 200
#         offset += 200
#         if resid > 0:
#             print(resid)

#         for message in messages_all['items']:
#             if message['from_id'] in ID_LISTS.keys():
#                 if message['text'] != '':
#                     ID_LISTS[message['from_id']].append(
#                         [message['text']])

#     for key, value in ID_LISTS.items():
#         value.reverse()
#         a.post_messages(IDS_NAMES[key], value)


# main()
