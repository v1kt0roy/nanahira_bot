# 七平bot

<div align=center><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/nnhr.jpg"  /></div>

## 开发缘由

>>本bot最开始应用于nanahira的粉丝群,用于推送曲子与群友互动,原本基于酷q+http-api,在酷q停止运营后转移使用[mirai-http-api](https://github.com/project-mirai/mirai-api-http)和[graia](https://github.com/GraiaProject),目前仍在完善功能。

## 如何使用
>>需要java和python运行环境,并手动修改miraihttp的initialkey(realease内为Nanahirabot0831),在运行mirai后，运行bot.py
>>* 查看bot所有指令的指令是/help
>>* 本bot定制性较强,最好在完整阅读完readme后再使用。
>>* 本bot所有功能均面向群聊，且不会涉及点赞 自动加好友 自动加群等敏感操作
## 主要功能
### 通用功能
>>* 本地图库调用
>>* 匹配聊天内容发图
>>* 求签
>>* 浅草寺求签
>>* 塔罗牌
>>* 骰娘相关功能（不全）
>>* 闲聊功能
>>* 图片api
>>* 复读
>>* 基本的开关bot功能
### 特色功能
>>* 推送歌曲
>>* 答题功能
>>* 影之诗语音（目前由于mirai http的原因暂时无法使用）
## 功能具体介绍
### 基本功能
#### 本地图库功能
>>在本地的image/目录下新建文件夹并传入图片，群内发送/+文件夹名即可以向群发送文件夹内的图片
>>* image目录下的文件夹名结尾不可以包含数字
>>* 如果在调用的指令后加入数字则可以返回复数张图片（最多为5，超过的按5张发送，发送负数则不会发送）
>>* 支持jpg png gif
>>* 使用/num+文件名即可返回image/文件名 目录下文件数目  
>>* 根目录下有一默认的setu文件夹，/color 调用里头的图片，内置了图片处理功能，可以绕开风控，谨慎使用
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp1.png"  /></div>
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp2.png"  /></div>
#### 匹配聊天内容发图
>>根目录下有message和message2两个文件夹，当有消息与message内的图片的文件名字完全匹配的时候，发送对应图片，当有消息内包含message2内图片对应文件名时，发送对应图片
>>* 上为message内名字为？.jpg的文件，下为message2内名字为好耶.jpg的图片
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp13.png"  /></div>
#### 求签
>>发送/求签+所求事项即可向机器人求签
>>* 同一天在同一个群内如果求同一事项，结果不变
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp3.png"  /></div>
#### 浅草寺求签
>>发送/浅草寺求签即可向机器人求签
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp4.png"  /></div>
#### 塔罗牌
>>发送/draw 或/adraw 即可抽一张塔罗牌
>>* /draw 抽取大阿卡纳牌（即熟知的22张牌中的一张）
>>* /adraw 从所有中抽取一张（包含小阿卡纳牌）
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp5.png"  /></div>
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp6.png"  /></div>
#### 骰娘
>>因为网上有很成熟的骰娘，目前只做了/dnd /coc生成角色，奖惩骰普通骰及暗骰，能用，但是如果需要好的体验请使用专业骰娘，查看相关功能发送/dicehelp
#### 闲聊
>>采用了腾讯的[闲聊api](https://ai.qq.com/product/nlpchat.shtml)，如要使用该功能，请自行向腾讯申请接口并修改tencent_chat.py内的app_id和app_key
>>调用方法有两种，群里聊天时机器人会有5%的概率回复或者直接发送/聊天+想和机器人聊天的内容来和机器人聊天
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp7.png"  /></div>
#### 图片api
>>/pic 从网络接口调用返回一张动漫图片
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp8.png"  /></div>
#### 复读
>>字面意思，当群内有同一消息被连续发送达到3次机器人即会开始复读
>>* 仅支持文字消息
#### 开关bot
>> /open /close即可开关bot /close情况下bot将不会响应/open以外的指令，并将在bot重启时保持之前的开关状态
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp9.png"  /></div>
### 特色功能
#### 歌曲推送
>>/来点na曲推送一首nanahira的曲子
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp10.png"  /></div>
#### 答题功能
>>/出题 出一个关于nanahira的题目，/答题+答案可以回答
>>* 填空题回答空可以直接看答案
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp11.png"  /></div>
#### 影之诗语音
>>/szb 返回一个影之诗ptsd语音
>>* 监修中
## 特别感谢
>>* [ななひら放送会](https://space.bilibili.com/498898366?from=search&seid=7710555003553182683)
>>* ななひら同好会群
>>* ななひら组的各位成员
>>* mirai和graia的开发人员
>>* 永喂不饱小小五（喵田弥夜群bot开发）
