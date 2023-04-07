# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('OTAyOTE2NTcwOTY2Mjc0MDU4.Gk2rzB.ym44fF9diVveVASWSyYupvfmKKJMnMvCN2IQIA')

client = discord.Client()

@client.event
async def on_ready(self):
    print(f'{self.client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

# A Default event
@client.event
async def on_message(self, message):
    if message.author == self.client.user:
        return

    if message.content == '99!':
        await message.channel.send('test')


client.run(TOKEN)
