from urllib import response
import discord
import os
from dotenv import load_dotenv
import get_spotify
import get_youtube
import get_tocxic_chick_soup
import random
from Server import keep_alive
import get_course
from replit import db
import time
import csv

load_dotenv('TOKEN.env')
client = discord.Client()

todaysFortune = ['大吉','中吉','末吉','小吉','大凶','小凶']
things = ['工作','学习','睡午觉','看番','看电影','通宵','打游戏','购物','装逼','卖弱','考试','摸鱼','创作','战斗','寻找爱情','成为猛男','早睡','哼哼啊啊啊啊啊啊啊啊','晚睡','锻炼','手舂']

@client.event
async def on_ready():
    print('Ready ({0.user})'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('/random song'):
        rdsong = get_spotify.get_track()

        await message.channel.send(rdsong)

    elif message.content.startswith('/help'):
        await message.channel.send('【/hello】 : Say hello~ \n【/random song】 : Random song from Spotify (API restricted)\n【/random video】 : Random video from Youtube \n【/c + course code】 : General Education courses information in Penn State.\n【/今日运势】 : 查看今日运势 \n【/签到】 : 签到\n【/推荐游戏】: 随机推荐游戏\n【/毒鸡汤】: 获取您今日份的毒鸡汤' )

    elif message.content.startswith('/今日运势'):
        yi = str(things[random.randint(0,len(things)-1)]) + '】'
        ji = str(things[random.randint(0,len(things)-1)]) + '】'
        while yi == ji:
            ji = str(things[random.randint(0,len(things)-1)]) + '】'
        await message.channel.send('今日运势: 【' + todaysFortune[random.randint(0,5)] + '】'+\
        '\n今日幸运数字: 【' + str(random.randint(0,9)) + '】'+\
        '\n宜【' + yi+\
        '\n忌【' + ji)

    elif message.content.startswith('/random video'):
        rdvideo = get_youtube.get_url()
        await message.channel.send(rdvideo)      

    elif message.content.startswith('/c'):
        strList = []
        intList = []
        content = list(message.content)[3:]
        for x in content:
            if content[0].isdigit() == False:
                strList.append(content[0])
                content = content[1:]

            else:
                break

        for i in content:
            intList.append(i)
        courseInfo = get_course.get_course(''.join(strList), ''.join(intList))
        await message.channel.send(courseInfo) 
            
    elif message.content.startswith('/签到'):
        id = str(message.author.id)
        localtime = time.strftime("%d",time.localtime())
        print(localtime)
        info = []
        if id not in db.keys():
            info.append("1")
            info.append(localtime)
            db[id] = info
            value_sign = db[id][0]
            await message.channel.send("签到成功！\n已签到【" + value_sign + "】天")
            
        else:
            if db[id][1] == localtime:                
                await message.channel.send("今日已经签到过了哟～\n签到天数:【" + db[id][0] + "】天")
            else:
                days = int(db[id][0])
                days += 1
                info.append(days)
                info.append(localtime)
                db[id] = info
        
                value_sign = str(db[id][0])
                await message.channel.send("签到成功！\n已签到【" + value_sign + "】天")

    elif message.content.startswith('/推荐游戏'):
        with open("./VideoGames.csv") as f:
            reader = csv.reader(f)
            result = list(reader)
            result = result[random.randint(1,16718)]
            await message.channel.send("游戏名称:【 " + result[0] + " 】\n平台:【 " + result[1] + " 】\n发布日期:【 " + result[2] + " 】\n类型:【 " + result[3] + " 】\n发布者:【 " + result[4] + " 】")

    elif message.content.startswith("/毒鸡汤"):
        soup = get_tocxic_chick_soup.get_soup()
        await message.channel.send(soup)

try:
    keep_alive()
    client.run(os.getenv('TOKEN'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')
