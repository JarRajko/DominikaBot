import discord


from discord.ext import commands

class Help(commands.Cog):



    @commands.Cog.listener()
    async def on_message(self, message):
      pass
        



    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Help(bot))
