# 七平bot

<div align=center><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/nnhr.jpg"  /></div>

## 开发缘由

>>本bot最开始应用于nanahira的粉丝群,用于推送曲子与群友互动,原本基于酷q+http-api,在酷q停止运营后转移使用[mirai-http-api](https://github.com/project-mirai/mirai-api-http)和[graia](https://github.com/GraiaProject),目前仍在完善功能。

## 如何使用
>>需要java和python运行环境,并手动修改miraihttp的initialkey(realease内为Nanahirabot0831),在运行mirai后，运行bot.py
>>* 本bot定制性较强,最好在完整阅读完readme后再使用。
## 主要功能
### 通用功能
>>* 本地图库调用
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
### 本地图库功能
>>在本地的image/目录下新建文件夹并传入图片，群内发送/+文件夹名即可以向群发送文件夹内的图片
>>* image目录下的文件名结尾不可以包含数字
>>* 如果在文件名后加入数字则可以返回复数张图片（最多为5，超过的按5张发送，发送负数则不会发送）
>>* 支持jpg png gif
>>* 使用/num+文件名即可返回image/文件名 目录下文件数目  
>>* 根目录下有一默认的setu文件夹，/color 调用，内置了图片处理功能，可以绕开风控，谨慎使用
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp1.png"  /></div>
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp2.png"  /></div>
### 求签
>>发送/求签+所求事项即可向机器人求签
>>* 同一天在同一个群内如果求同一事项，结果不变
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp3.png"  /></div>
### 浅草寺求签
>>发送/浅草寺求签即可向机器人求签
>><div><img src="https://github.com/v1kt0roy/nanahira_bot/raw/main/image/exp4.png"  /></div>
###
