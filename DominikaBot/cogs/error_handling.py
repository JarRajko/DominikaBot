import discord
import os
import random

from discord.ext import commands

class Error_Handling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandNotFound):
            filename = "./speech/unknown_command.txt"
            f = open(filename,"r",encoding="utf8")
            content = f.readlines()
            await ctx.send(random.choice(content))
        else:
            await ctx.send(error) # <<< 


    #@commands.Cog.listener()
            #@bot.command() #Checking the lattency of our bot
    #async def ping(ctx): #CTX - context some sort of data obtained automatically
    #    await ctx.send(f'Pong! Haha to je vtip, ktorý ti dôjde asi za {round(bot.latency * 1000)} milisekúnd.')

#@clr.error
#async def clr_error(ctx, error):
#    if isinstance(error, commands.errors.MissingPermissions):
#        pass
#    else:
#        await ctx.send("Fajne! Ale skús to ešte raz a spomeň aj nejaké konkrétne číslo.")



def setup(bot):
    bot.add_cog(Error_Handling(bot))
