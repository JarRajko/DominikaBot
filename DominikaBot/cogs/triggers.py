import discord
import os
import random

from discord.ext import commands

class Triggers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    
    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        await bot.send_message(channel,content = "OKKK")
        
    

def setup(bot):
    bot.add_cog(Triggers(bot))