from urllib import response
import discord
import os
from dotenv import load_dotenv
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

    elif message.content.startswith('/help'):
        await message.channel.send('/hello : Say hello~ \n/random song : A random song from Spotify')

client.run(os.getenv('TOKEN'))
