#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:59:22 2019

@author: alexliu
"""


import requests
import itchat

def SentChatRoomsMsg(name, context):
    itchat.get_chatrooms(update=True)
    iRoom = itchat.search_chatrooms(name)
    print(iRoom)
    for room in iRoom:
        if room['NickName'] == name:
            userName = room['UserName']
            print("--------=======--------"+userName)
            break
    itchat.send_msg(context, userName)
    print("*********************************************************************************")

def loginCallback():
    print("***登录成功***")

def exitCallback():
    print("***已退出***")


itchat.auto_login(hotReload=True, enableCmdQR=2, loginCallback=loginCallback, exitCallback=exitCallback)
roomslist = itchat.get_contact(update=True)
print(roomslist)

#发送内容
context =  """
Hello,world!
"""

SR_info = []
#A类交易所信息
exchange_a = []
#B类交易所信息
exchange_b = []
#钱包信息
wallet =  []

#调整要发送的目标
list_name = wallet

for i in range(0, len(list_name)):
    name = list_name[i]
    context = context
    print("----------------第 "+str(i+1)+" 次---------------")
    try:
        SentChatRoomsMsg(name,context)
    except:
        SentChatRoomsMsg(name,context)
