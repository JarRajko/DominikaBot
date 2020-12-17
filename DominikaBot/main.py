import discord 
import random
import os
import json

from discord.ext import commands, tasks
from itertools import cycle


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = 'Dominika? ', intents = intents)

@bot.event
async def on_ready():
    print("Dominika is online.")
    print('Logged in as ---->', bot.user)
    print('ID:', bot.user.id)
    #await client.change_presence(activity=discord.Game(name='my game'))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" you!"))

@bot.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('.\cogs')    :
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')    
        print("Loaded extension: " + str(filename))
        
def is_check_user(ctx): #Check user
    return ctx.author.id == 604630490225573898

@bot.command()
@commands.check(is_check_user) #Check user
async def testicek(ctx):
    channel = bot.get_channel(786223537395597356)
    await ctx.send("Yes masťer.")
    await ctx.send(ctx.guild.id)
    await channel.send("REEEEEEEE")
    


#@tasks.loop(seconds=1800)
#async def change_status():
#    await bot.change_presence(activity=discord.Game(next(status)))

def setup(bot):
    bot.add_cog(Example(bot))

    
bot.run('NzgzMDIwNjIwNDUwODg5NzM5.X8Uqxw.O5_xj7SuQBJtR49VFkbynsOW26c')    
