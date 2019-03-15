# pylint: disable=no-member

import sys, os
sys.path.append("../")
import random
import itchat
from datetime import datetime
from log_output import ptLg
from util import zan_list
# from weChat.weather.weather import getWeather

@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    NickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    toWho = itchat.search_friends(userName=msg['ToUserName'])['NickName']
    if '夸我' in msg['Text']:
        zan = random.choice(zan_list)
        itchat.send('%s'%zan, msg['FromUserName'])
        ptLg('我回复给' + NickName + '的消息:' + zan)
        ptLg(NickName+ '发给' + toWho + '的消息:' + msg['Text'])
    if '天气' in msg['Text']:
    	city = msg['Text'].replace('天气','')
    	weather_res = getWeather(city)
    	itchat.send('%s'%weather_res, msg['FromUserName'])
    	ptLg('我回复给' + NickName + '的消息:' + weather_res)
# itchat.auto_login(hotReload=True) # 热启动，不需要多次扫码登录
# itchat.auto_login() # 热启动，不需要多次扫码登录
# itchat.run()

print(sys.path)