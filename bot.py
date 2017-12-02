
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
	if message.author == bot.user:
		return
	if message.server == None and message.content == "!read":
			app_id= '306163839896677'
			app_secret= 'b46fed8fbb1539af3827de7009c750a8'
			access_token= app_id + "|" + app_secret
			page_name = input("Please enter your facebook page url: ")
			graph = facebook.GraphAPI(access_token, 2.11)#Request access

			site_info =  graph.get_object(id=page_name, field= 'message') #Get id of page
			post =  graph.get_connections(id=site_info["id"], connection_name = 'posts') #Get posts of page

			post = post['data'][0]['message']


			post_data = open('post_data.txt','wb')
			post_data.write(post.encode("UTF-8")) #Saves the most recent post in file
			post_data.close()
			with open ('post_data.txt') as f:
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
	if message.content == '!setPost':
		w = open("channel.txt", "w")
		w.write(str(message.channel.id))
		w.close()
       

bot.run('MzU3NzIzNzYyMDkyODAyMDUw.DQP9Eg.K4m6VXRtCZMlvvO53uE51mraANs')
