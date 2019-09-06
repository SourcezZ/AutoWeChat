# pylint: disable=no-member

from funcPy.chat_with_tuling import chat_with_tuling
from funcPy.my_logger import logger
from datetime import datetime
import itchat
import sys
import os
sys.path.append("..")


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def text_reply(msg):
    NickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    if NickName == 'Ideao':
        sendMsg = chat_with_tuling(msg['Text'])
        itchat.send('%s' % (sendMsg), msg['FromUserName'])
        logger.info('Source' + '发给' + NickName + '的消息:' + sendMsg)
    if msg['ToUserName'] != 'filehelper':
        toWho = itchat.search_friends(userName=msg['ToUserName'])['NickName']
        logger.info(NickName + '发给' + toWho + '的消息:' + msg['Text'])
    else:
        logger.info(NickName + '发给filehelper的消息:' + msg['Text'])
        # itchat.send('%s'%(msg['Text']), msg['FromUserName'])

        # return msg['Text']


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    NickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    # 下载图片
    df = datetime.now().strftime('%m%d%H%M%S')
    logger.info('图片下载:' + NickName + '_' + df + '.' + str(msg.FileName).split('.')[1])
    if not os.path.isdir('itChatImg/' + NickName):
        logger.info('新的用户消息,创建用户文件夹:' + NickName)
        os.makedirs('itChatImg/' + NickName)
    msg.download('./itChatImg/' + NickName + '/' + NickName + '_' + df + '.' + str(msg.FileName).split('.')[1])

    # 发送图片
    # itchat.send('@img@%s' % (msg['FileName']),msg['FromUserName'])


@itchat.msg_register(['Text', 'Picture'], isGroupChat=True)
def download_files_group(msg):
    NickName = msg.ActualNickName
    GroupName = msg['User']['NickName']
    if msg.Type == 'Text':
        logger.info('群消息 [' + GroupName + '] 群组的 [' + NickName + '] 发来的 : ' + msg['Text'])
    elif msg.Type == 'Picture':
        # 下载图片
        df = datetime.now().strftime('%m%d%H%M%S')
        logger.info('群消息 [' + GroupName + '] 群组的 [' + NickName + '] 发来的图片,保存为' + str(df) + '.jpg')
        if not os.path.isdir('itChatImg/Group/' + GroupName):
            logger.info('新的群组,创建Group下的文件夹:' + GroupName)
            os.makedirs('itChatImg/Group/' + GroupName)
        msg.download('./itChatImg/Group/' + GroupName + '/' + NickName + '_' + df + '.jpg')


# @itchat.msg_register('Text', isGroupChat = True)
# def text_reply(msg):
#     if msg['isAt']:
#         itchat.send(u'@%s\u2005I received: %s'%(msg['ActualNickName'], msg['Content']), msg['FromUserName'])
itchat.auto_login(hotReload=True)  # 热启动，不需要多次扫码登录
itchat.run()
