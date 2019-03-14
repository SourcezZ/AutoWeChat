# pylint: disable=no-member

import sys, os
sys.path.append("..")
import random
import itchat
from datetime import datetime
from log_output import ptLg
from util import zan_list

@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    NickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    if '夸我' in msg['Text']:
        toWho = itchat.search_friends(userName=msg['ToUserName'])['NickName']
        ptLg(NickName+ '发给' + toWho + '的消息:' + msg['Text'])
        zan = random.choice(zan_list)
        itchat.send('%s'%zan, msg['FromUserName'])
        ptLg('我回复给' + NickName + '的消息:' + zan)
itchat.auto_login(hotReload=True) # 热启动，不需要多次扫码登录
# itchat.auto_login() # 热启动，不需要多次扫码登录
itchat.run()