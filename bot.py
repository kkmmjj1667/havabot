#기본 import 
import discord


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

        

client.run("NzU1NTgxMTQ0NDEzNjM0NTcy.X2FXxg.6U0UtxkdVVLnBZHVv34TqK6G2Hc")