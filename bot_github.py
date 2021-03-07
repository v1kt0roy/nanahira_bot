# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:46:05 2021

@author: v1kt0r
"""

import hashlib
import time
import string
from urllib.parse import quote
 
def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    return m.hexdigest().upper()
 
def get_params(plus_item):
    global params
    t = time.time()
    time_stamp=str(int(t))  
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # 应用标志，这里修改成自己的id和key  
    app_id=''
    app_key=''
    params = {'app_id':app_id,
              'question':plus_item,
              'time_stamp':time_stamp,
              'nonce_str':nonce_str,
              'session':'10000'
             }
    sign_before = ''
    #要对key排序再拼接
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
        sign_before += '{}={}&'.format(key,quote(params[key], safe=''))
    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
    sign_before += 'app_key={}'.format(app_key)
    # 对字符串sign_before进行MD5运算，得到接口请求签名  
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params
 
import requests
 
def get_content(plus_item):
    global payload,r
    # 聊天的API地址  
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    # 获取请求参数  
    plus_item = plus_item.encode('utf-8')
    payload = get_params(plus_item)
    # r = requests.get(url,params=payload)  
    r = requests.post(url,data=payload)
    return r.json()["data"]["answer"]




#保持
import nest_asyncio
nest_asyncio.apply()
import random

import asyncio
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication
from graia.application.message.elements.internal import At, Plain
from graia.application.session import Session
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.broadcast.interrupt import InterruptControl
from graia.broadcast.interrupt.waiter import Waiter
from graia.application.event.messages import GroupMessage
from graia.application.friend import Friend
from graia.application.message.parser.kanata import Kanata
from graia.application.message.parser.signature import FullMatch, OptionalParam, RequireParam
loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8080", # 填入 httpapi 服务运行的地址
        authKey="INITKEYwqJ2AgjK", # 填入 authKey
        account=2917132849, # 你的机器人的 qq 号
        websocket=True # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)
inc = InterruptControl(bcc)
@bcc.receiver("FriendMessage")
async def friend_message_handler(message:MessageChain,app: GraiaMiraiApplication, friend: Friend):
        await app.sendFriendMessage(friend, MessageChain.create([
            Plain()
        ]))

@bcc.receiver("GroupMessage")
async def group_message_handler(
    message: MessageChain,
    app: GraiaMiraiApplication,
    group: Group, member: Member,
):
    if message.asDisplay().startswith("/help"):
         await app.sendGroupMessage(group, MessageChain.create([
            Plain("/dnd /coc 人物卡属性生成\n/rb奖励骰 /rp惩罚骰")
            ]))
#跑团相关
    if message.asDisplay().startswith("/dnd"):
        dnd_point=[]
        for n in range(1,7):
            single=[]
            for i in range(1,5):
                single.append(random.randint(1,6))
            single.sort()
            dnd_point.append(sum(single)-single[0])
        dnd_rolloutput="力量："+str(dnd_point[0])+"体质："+str(dnd_point[1])+"敏捷："+str(dnd_point[2])+"智力："+str(dnd_point[3])+"感知："+str(dnd_point[4])+"魅力："+str(dnd_point[5])+"总计"+str(sum(dnd_point))
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),Plain(dnd_rolloutput)
        ]))
    if message.asDisplay().startswith("/coc"):
        coc_point=[]
        for n in range(1,10):
            if len(coc_point)<=3:
                point=0
                for i in range(1,3):
                    point+=random.randint(1,6)
                coc_point.append(5*(point+6))
            else:
                point=0
                for i in range(1,4):
                    point+=random.randint(1,6)
                coc_point.append(5*point)
        rolloutput="力量："+str(coc_point[3])+"体质："+str(coc_point[4])+"体型："+str(coc_point[0])+"敏捷："+str(coc_point[5])+"外貌："+str(coc_point[6])+"智力："+str(coc_point[1])+"意志："+str(coc_point[7])+"教育："+str(coc_point[2])+"幸运："+str(coc_point[8])+"总计"+str(sum(coc_point)-coc_point[8])+"/"+str(sum(coc_point))
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),Plain(rolloutput)
        ]))
    if message.asDisplay().startswith("/rp"):
        a=random.randint(0, 9)
        b=random.randint(0, 9)
        if a<b:
            a=b
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),Plain("骰了一次惩罚骰，点数为"+str(a*10+random.randint(0, 9)))
        ]))
    if message.asDisplay().startswith("/rb"):
        a=random.randint(0, 9)
        b=random.randint(0, 9)
        if a>b:
            a=b
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),Plain("骰了一次奖励骰，点数为"+str(a*10+random.randint(0, 9)))
        ]))
#qq闲聊
    if message.asDisplay().startswith("/聊天"):
        await app.sendGroupMessage(group, MessageChain.create([
            At(member.id),Plain(str(get_content(message.asDisplay().strip("/聊天").strip())))
        ]))
app.launch_blocking()





