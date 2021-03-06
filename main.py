#!/usr/bin/env python3
# coding:utf-8

import os
import re
import sys
import django
import asyncio
import datetime
import websockets
from django.conf import settings
from asgiref.sync import sync_to_async
from bilibili_api import live, sync
room = live.LiveDanmaku(3472667)

async def hello(name):
    uri = "ws://live.mineraltown.net:5678"
    async with websockets.connect(uri) as websocket:
        await websocket.send(name)

@sync_to_async
def django_(msg):
    # UID
    uid = msg['data']['info'][2][0]
    # 昵称
    name = msg['data']['info'][2][1]
    # 弹幕
    danmu = msg['data']['info'][1]
    # 粉丝勋章
    medal_name = msg['data']['info'][3]
    if medal_name != []:
        if medal_name[1] == '芜菁' or  medal_name[1] == '折染' :
            vip = True
        else :
            vip = False
    else :
        vip = False
    # 大航海
    dahanghai = msg['data']['info'][7]
    if dahanghai != 0:
        svip = True
    else:
        svip = False
    # 指令弹幕分析
    if danmu[0] == '#' or danmu[0] == '＃' :
        user = search(uid,name)
        if user == None:
            add_return = add(uid=uid,name=name)
            user = search(uid,name)
            log(user,add_return)
        command_return = command(user,danmu[1:].strip(),vip,svip)
        if command_return not in ['已签到','体力','积分','命令']:
            log(user,command_return)
        return_msg = '<snap class="info">' + str(name) + str(command_return) + '</snap>'
    else:
        return_msg = '<snap class="name">' + str(name) + '：</snap><snap class="msg">' + str(danmu) + '</snap>'
    return return_msg

@sync_to_async
def django_gift(msg):
    action = msg['data']['data']['action']
    giftName = msg['data']['data']['giftName']
    uid = msg['data']['data']['uid']
    name = msg['data']['data']['uname']
    num = msg['data']['data']['num']
    price = msg['data']['data']['price']
    user = search(uid,name)
    # 免费礼物额外判定
    if giftName == '辣条':
        price=10
    elif giftName == '小心心':
        price=100
    if user == None:
        add_return = add(uid=uid,name=name)
        user = search(uid,name)
        log(user,add_return)
    user.gold = user.gold + price * num
    log(user,action + '了' + giftName + '×' + str(num) + '，积分+' + str(price * num))
    user.save()

# 弹幕
@room.on("DANMU_MSG")
async def on_danmu(msg):
    a = await django_(msg)
    await hello(a)
    with open("muchang_live.log", "a", encoding="utf-8") as f:
        d = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.writelines(d + ' > ' + msg['data']['info'][2][1] + ':' + msg['data']['info'][1] + '\n')
        if 'class="msg"' not in a:
            f.writelines(d + ' < ' + re.sub('<.*?>','',a) + '\n')

# 礼物
@room.on("SEND_GIFT")
async def send_gift(msg):
    await django_gift(msg)

async def main():
    await room.connect()

if __name__ == "__main__": 
    sys.path.append(os.getcwd())
    os.chdir(os.getcwd())
    os.environ['DJANGO_SETTINGS_MODULE'] = 'muchang_live.settings'
    django.setup()
    from danmaku.tools import *
    asyncio.run(main())
