from urllib import response
import discord
import os
from dotenv import load_dotenv
import get_spotify
import get_youtube
import random

load_dotenv('TOKEN.env')
client = discord.Client()

todaysFortune = ['大吉','中吉','末吉','小吉','大凶','小凶']


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
        await message.channel.send('/hello : Say hello~ \n/random song : A random song from Spotify \n/今日运势 : 查看今日运势 \n/random video : A random video from Youtube' )

    elif message.content.startswith('/今日运势'):
        await message.channel.send('今日运势: 【' + todaysFortune[random.randint(0,5)] + '】\nLucky number today: 【' + str(random.randint(0,9)) + '】')

    elif message.content.startswith('/random video'):
        rdvideo = get_youtube.get_url()
        await message.channel.send(rdvideo)        

client.run(os.getenv('TOKEN'))
