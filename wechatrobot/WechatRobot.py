import itchat
import time
from itchat.content import *
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def Login():
    itchat.auto_login(hotReload=True, enableCmdQR=2)

# 1/Functionalize sending message
# 2/Make confidential info inputs


# Login()
flag_func = 2
MyNickName = "CYH Jon"

List2Reply = ["一环","木马"]
reply_code = 2  # 0: none; 1: repeat; 2:AI


def ModifyMessage(msg: str, i: int):
    return msg+str(i)


def Check():
    itchat.check_login()


def Run():
    itchat.run()


def LogOut():
    itchat.logout()


bot = ChatBot("ChineseChatbot1")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.chinese")


@itchat.msg_register(TEXT)
def text_reply(msg):
    author = itchat.search_friends(userName=msg.fromUserName)
    print('!!=%s(%s)=!!' % (author["NickName"], author["RemarkName"]))
    print("  ", end="")
    print(msg.text)
    if (author["RemarkName"] in List2Reply) or (author["NickName"] in List2Reply):
        if reply_code == 1:
            msg_ = msg.text+" (我是无情复读机)"
        elif reply_code == 2:
            msg_ = bot.get_response(msg.text)
            msg_ = str(msg_)
        else:
            msg_ = ""

        if author["NickName"] == MyNickName:
            itchat.send(msg_, toUserName="filehelper")
        else:
            time.sleep(1)
            # print(msg_)
            author.send(msg_)


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    # print(msg.isAt)
    print('--=%s=--' % msg.actualNickName)
    print("  ", end="")
    print(msg.content)


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    author = itchat.search_friends(userName=msg.fromUserName)
    print('!!=%s(%s)=!!' % (author["NickName"], author["RemarkName"]))
    print("  ", end="")
    print('@%s@%s' % (typeSymbol, msg.fileName))
    return '@%s@%s' % (typeSymbol, msg.fileName)

# @itchat.msg_register(ATTACHMENT)
# def download_files(msg):
#     msg['Text'](msg['FileName'])


# Settings #
# 1. Send a message or file to filehelper
if flag_func == 1:
    user_name = "filehelper"
    msg = "?"
    # msg = '@img@%s' % '/Users/YuhangChen/Downloads/test.png'
    # itchat.send('@fil@%s' % 'xlsx.xlsx')
    # itchat.send('@vid@%s' % 'demo.mp4')

    n_msg = 1
    msg_interval = 1  # in seconds

# 2. Send a message or file multiple times
if flag_func == 2:
    name = "CYH Jon"
    msg = "xue"
    # address = "/Users/YuhangChen/Desktop/Screen Shot 2019-03-30 at 00.34.37.png"
    # msg = '@img@%s' % address
    n_msg = 2
    msg_interval = 1  # in seconds
    hold_before_send = 0  # in seconds


# Function Implementation #
# 1. Send a file to filehelper
if flag_func == 1:
    for i in range(n_msg):
        msg_ = ModifyMessage(msg, i)
        itchat.send(msg_, toUserName=user_name)
        time.sleep(msg_interval)


# 2. Send a message multiple times
if flag_func == 2:
    user_list = itchat.search_friends(name=name)
    author = user_list[0]
    # user_name = author["UserName"]
    if len(user_list) != 1:
        print("The length of user list is "+str(len(user_list)))
    else:
        time.sleep(hold_before_send)
        for i in range(n_msg):
            msg_ = ModifyMessage(msg, i+1)
            author.send(msg_)
            time.sleep(msg_interval)

# 3. Receive messages
if flag_func == 3:
    pass


# itchat.search_friends()
# itchat.search_friends(name="wrk1231")
# user_list = itchat.search_friends(name="王瑞康")
# user_name = a[0]["UserName"]
# print(user_name)
# itchat.check_login()
