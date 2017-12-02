
import discord
from discord.ext import commands
import random


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def read():
    """Chooses between multiple choices."""
    with open ('post.txt') as f:
        data = f.readlines()

    for line in data:
        words = line.split()
        if words == []:
            continue
        else:
            words += "\n"
            words = " ".join(words) 
            await bot.say(words)

    f.close()


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    if save != None:
        await bot.send_message(message.channel, message.content)
    if message.content.startswith('!live'):
        save = message.channel
        await bot.send_message(message.channel, "saved")
    

       
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

bot.run('MzU3NzIzNzYyMDkyODAyMDUw.DQP9Eg.K4m6VXRtCZMlvvO53uE51mraANs')
