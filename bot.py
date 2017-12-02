
import discord
from discord.ext import commands
import random
import sys


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.server == None and message.content == "!read":
        with open ('post.txt') as f:
            data = f.readlines()
        for line in data:
            words = line.split()
            if words == []:
               continue
        else:
            words += "\n"
            words = " ".join(words) 
            await bot.send_message(discord.Object(id=line), words)
        f.close()
    if message.server == None:
        f = open("channel.txt", "r")
        line = f.readline()
        line = line.strip("\n")
        await bot.send_message(discord.Object(id=line),message.content)
        f.close()
        w = open("post.txt", "w")
        w.write(message.content)
        w.close()
    if message.content == '!setPost':
        w = open("channel.txt", "w")
        w.write(str(message.channel.id))
        w.close()
       

bot.run('MzU3NzIzNzYyMDkyODAyMDUw.DQP9Eg.K4m6VXRtCZMlvvO53uE51mraANs')
