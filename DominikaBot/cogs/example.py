import discord
import asyncio

from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() #If you want to create an event within a cog, you always have to use this decorator
    async def on_ready(self): #Self must be an argument that every function inside of your class takes
        print("Dominika is online.")
        #await client.change_presence(activity=discord.Game(name='my game'))
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" you!"))

    @commands.command() #Command decorator
    async def ping(self, ctx):
        await ctx.send(f'Pong!')
        await asyncio.sleep(self.bot.latency )
        await ctx.send(f' Haha to je vtip, ktorý ti dôjde asi za {round(self.bot.latency * 1000)} milisekúnd.')
def setup(bot):
    bot.add_cog(Example(bot))
