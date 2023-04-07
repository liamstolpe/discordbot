# bot.py
import os
import random
import discord
import json
from dotenv import load_dotenv

# Opens the file in read-only mode and assigns the contents to the variable cfg to be accessed further down
with open('config.json', 'r') as cfg:
  # Deserialize the JSON data (essentially turning it into a Python dictionary object so we can use it in our code) 
  data = json.load(cfg) 
# Where you'd normally log in, replace your token string with: data["token"]

load_dotenv()
TOKEN = os.getenv(data["token"])

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
