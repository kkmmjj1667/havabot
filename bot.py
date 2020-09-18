import discord
import os


import os
import pyautogui

client = discord.Client()

@client.event

async def on_ready():
    print("ready")

@client.event

async def on_message(message):
 
    if message.content.startswith('!screen'):
      
        img = pyautogui.screenshot("0.png")
     
        await message.channel.send(file=discord.File("0.png"))
     
        os.remove("0.png")

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
