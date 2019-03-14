# pylint: disable=no-member
import sys
sys.path.append("..")

import itchat
from datetime import datetime
from funcPy.log_output import ptLg

def text_send(userName,isGroup):
    if('pushed' not in globals()):
        global pushed
        pushed = True
        print('当前给' + userName + '发送消息')
        
    # 获取任何一项等于name键值的用户
    if(isGroup == 1):
        User = itchat.search_chatrooms(name=userName)
    else:
        User = itchat.search_friends(name=userName)
    #获取发送目标ID
    toUserName = User[0].UserName

    #获取发送目标昵称
    NickName = User[0].NickName

    #发送内容
    text = input('\ntext:')
    ptLg('主动发送消息:给' + NickName + '发送消息:' + text)

    itchat.send('%s' % text, toUserName)
itchat.auto_login(hotReload=True) # 热启动，不需要多次扫码登录
name = input('who you want to send:')
isGroup = input('isGroup (1 or 0):')
while 1:
    text_send(name,isGroup)
    # text_send('W',False)