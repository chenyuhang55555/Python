from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# import urllib
# from bs4 import BeautifulSoup
import os

bot = ChatBot("Test")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.chinese")

while True:
    message = input("You:")
    if message.strip() != "Bye":
        reply = bot.get_response(message)
        print("ChatBot:", reply)
    else:
        print("ChatBot: Bye")

# message = input("You:")
# print(message)

# appid = 'K4HPAP-6AXE79P48P'  # 你的appid


# def answer(question):
#     serviceurl = 'http://api.wolframalpha.com/v2/result?'
#     url = serviceurl + \
#         urllib.parse.urlencode({'appid': appid, 'input': question,
#                                 'timeout': '5'})  # 设置一个timeout
#     for i in range(3):
#         # print(url)
#         try:
#             uh = urllib.request.urlopen(url)
#         except:
#             print("Error in URL open!")
#             time.sleep(1)
#             continue
#         if uh.getcode() != 200:
#             print("Query failure!")
#             time.sleep(1)
#             continue
#         soup = BeautifulSoup(uh, 'lxml')
#         short_answer = soup.get_text()
#         print(short_answer)
#         if 'No short answer' in short_answer:
#             return "Sorry, please ask an easy question in English"
#         return short_answer
#     return "I have a headache now. Talk later."