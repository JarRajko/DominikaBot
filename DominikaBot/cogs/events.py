import discord
import json

from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Nechapem.')
        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.reactiongifs.com%2Fr%2F2013%2F08%2Fno-power.gif&f=1&nofb=1')
    #@bot.command() #Checking the lattency of our bot
    #async def ping(ctx): #CTX - context some sort of data obtained automatically
    #    await ctx.send(f'Pong! Haha to je vtip, ktorý ti dôjde asi za {round(bot.latency * 1000)} milisekúnd.')


def setup(bot):
    bot.add_cog(Events(bot))
