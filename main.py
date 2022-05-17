from urllib import response
import discord
import os
from dotenv import load_dotenv
import get_spotify
import get_youtube
import random
from Server import keep_alive
import get_course

load_dotenv('TOKEN.env')
client = discord.Client()

todaysFortune = ['大吉','中吉','末吉','小吉','大凶','小凶']
things = ['工作','学习','睡午觉','看番','看电影','打游戏','购物','秀恩爱','装逼','卖弱','考试','摸鱼','创作','战斗','寻找爱情','成为美少女','成为猛男','早睡','哼哼啊啊啊啊啊啊啊啊','搞基','百合','晚睡','锻炼','展示变态属性','手舂']


@client.event
async def on_ready():
    print('Ready ({0.user})'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('/random song'):
        rdsong = get_spotify.get_track()

        await message.channel.send(rdsong)

    elif message.content.startswith('!help'):
        await message.channel.send('【!hello】 : Say hello~ \n【!random song】 : Random song from Spotify (API restricted)\n【!今日运势】 : 查看今日运势 \n【!random video】 : Random video from Youtube \n【!c + course code】 : General Education courses information in Penn State.' )

    elif message.content.startswith('!今日运势'):
        yi = str(things[random.randint(0,len(things)-1)]) + '】'
        ji = str(things[random.randint(0,len(things)-1)]) + '】'
        while yi == ji:
            ji = str(things[random.randint(0,len(things)-1)]) + '】'
        await message.channel.send('今日运势: 【' + todaysFortune[random.randint(0,5)] + '】'+\
        '\n今日幸运数字: 【' + str(random.randint(0,9)) + '】'+\
        '\n宜【' + yi+\
        '\n忌【' + ji)

    elif message.content.startswith('!random video'):
        rdvideo = get_youtube.get_url()
        await message.channel.send(rdvideo)      

    elif message.content.startswith('!c'):
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
            

keep_alive()
client.run(os.getenv('TOKEN'))
