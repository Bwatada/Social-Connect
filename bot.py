
import discord
from discord.ext import commands
import random
import sys
import facebook


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
    print(message.content[:5])
    if message.author == bot.user:
        return
    if message.server == None and message.content[:5] == "!read":

        app_id= '306163839896677'
        app_secret= 'b46fed8fbb1539af3827de7009c750a8'
        access_token= app_id + "|" + app_secret
        page_name = message.content[6:]
        graph = facebook.GraphAPI(access_token, 2.11)#Request access
        site_info =  graph.get_object(id=page_name, field= 'message') #Get id of page
        post =  graph.get_connections(id=site_info["id"], connection_name = 'posts') #Get posts of page
        post = post['data'][0]['message']
        await bot.send_message(message.channel, post)

    if message.server == None:
        f = open("channel.txt", "r")
        line = f.readline()
        line = line.strip("\n")
        await bot.send_message(discord.Object(id=line),message.content)
    if message.content == '!setPost':
        w = open("channel.txt", "w")
        w.write(str(message.channel.id))
        w.close()
    if message.content[:5] == "!post":
        message = message.content[6:]
        cfg = {
        "page_id" : "1772893583011687",
        "access_token" : "EAACEdEose0cBAEAU3gsrqgrSpMtwKiJGWMef9yZCkzfc7PIaeummZBqUK9unzl2Ii7PqhtaJjtXXv9npiCcIaUhKMOnrZBLQZCsYXnzOIIqfIoKKA5VzWxJHuZA2DnfZB9NBKrirerceWY89lO7bfAOFF37HShqt6i8fn5byZAQ18GbMQemNire20lZBfvmKiTIe1R0iVPZBWZAwZDZD"
        }
        graph = facebook.GraphAPI(cfg["access_token"])
        resp = graph.get_object("me/accounts")
        page_access_token=None
        for page in resp["data"]:
        	if page["id"] == cfg["page_id"]:
        		page_access_token = page["access_token"]
        	graph = facebook.GraphAPI(page_access_token)
        success = graph.put_wall_post(message)

    if message.content == '!help':
        await bot.send_message(message.channel, "Usage: !setPost - sets the desired channel for announcements to be made !post [message]- posts entered message to predetermined facebook page. !read** - reads latest post from Facebook page and posts it in desired channel.")
        await bot.send_message(message.channel, "In order to use this bot, you must have the facebook module and discord.py modules installed. You must also be able to run the program in a terminal. We are planning to eventually host the bot on a server so you will be able to add it that way instead. When using the bot for the first time, use the command !setPost in the desired channel in order to tell the bot that this is where you would like all announcements to be posted. ")
bot.run('MzU3NzIzNzYyMDkyODAyMDUw.DQP9Eg.K4m6VXRtCZMlvvO53uE51mraANs')
