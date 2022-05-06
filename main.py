from urllib import response
import discord
import os
from dotenv import load_dotenv
import requests
import json
import random
import get_spotify

load_dotenv('TOKEN.env')
client = discord.Client()




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

client.run(os.getenv('TOKEN'))
