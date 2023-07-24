import discord 
import random
import os
import asyncio

from discord.ext import commands, tasks
from itertools import cycle

# zapne logovanie do konzoly
discord.utils.setup_logging()

#intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
intents = discord.Intents.all()
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

#@tasks.loop(seconds=1800)
#async def change_status():
#    await bot.change_presence(activity=discord.Game(next(status)))

#def setup(bot):
#    bot.add_cog(Example(bot))

async def main():
    async with bot:
        for filename in os.listdir('./cogs')    :
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')    
                print("Loaded extension: " + str(filename))

        f = open("token.txt",encoding="utf8")
        token = f.readlines()
        await bot.start(token[0])

asyncio.run(main())
