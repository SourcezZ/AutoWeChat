# pylint: disable=no-member

import sys, os
sys.path.append("..")

import itchat
from datetime import datetime
from funcPy.log_output import ptLg

@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    # print('cyd' if msg.FromUserName == cyd else 'hy','发来的消息:',msg['Text'])
    NickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    if msg['ToUserName']!='filehelper':
        toWho = itchat.search_friends(userName=msg['ToUserName'])['NickName']
        ptLg(NickName+ '发给' + toWho + '的消息:' + msg['Text'])
    else:
        ptLg(NickName+ '发给filehelper的消息:' + msg['Text'])
        # itchat.send('%s'%(msg['Text']), msg['FromUserName'])

        # 打印日志
        # if('pushed' not in globals()):
            # global pushed
            # pushed = True
            # print(msg)
        # return msg['Text']

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    # print('cyd' if msg.FromUserName == cyd else 'hy','发来的消息:',msg['Type'])
    NickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    #下载图片
    df = datetime.now().strftime('%m%d%H%M%S')
    ptLg('图片下载:' + NickName + '_' + df + '.' + str(msg.FileName).split('.')[1])
    if not os.path.isdir('itChatImg/' + NickName):
        ptLg('新的用户消息,创建用户文件夹:' + NickName)
        os.makedirs('itChatImg/' + NickName)
    msg.download('./itChatImg/' + NickName + '/' + NickName + '_' + df + '.' + str(msg.FileName).split('.')[1])

    # 发送图片
    # itchat.send('@img@%s' % (msg['FileName']),msg['FromUserName'])

    # 打印日志
    # if('pushedPic' not in globals()):
    #     global pushedPic
    #     pushedPic = True
    #     print(msg)

@itchat.msg_register(['Text','Picture'], isGroupChat = True)
def download_files_group(msg):
    NickName = msg.ActualNickName
    GroupName = msg['User']['NickName']
    if msg.Type == 'Text':
        # print('群消息 [', GroupName, '] 群组的 [' + NickName + '] 发来的 : ' + msg['Text'])
        ptLg('群消息 [' + GroupName + '] 群组的 [' + NickName + '] 发来的 : ' + msg['Text'])
    elif msg.Type == 'Picture':
        #下载图片
        df = datetime.now().strftime('%m%d%H%M%S')
        ptLg('群消息 [' + GroupName + '] 群组的 [' + NickName + '] 发来的图片,保存为' + str(df) + '.jpg')
        if not os.path.isdir('itChatImg/Group/' + GroupName):
            ptLg('新的群组,创建Group下的文件夹:' + GroupName)
            os.makedirs('itChatImg/Group/' + GroupName)
        msg.download('./itChatImg/Group/' + GroupName + '/' + NickName + '_' + df + '.jpg')
# @itchat.msg_register('Text', isGroupChat = True)
# def text_reply(msg):
#     if msg['isAt']:
#         itchat.send(u'@%s\u2005I received: %s'%(msg['ActualNickName'], msg['Content']), msg['FromUserName'])
itchat.auto_login(hotReload=True) # 热启动，不需要多次扫码登录
itchat.run()
