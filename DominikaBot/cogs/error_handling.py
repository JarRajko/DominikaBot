import discord


from discord.ext import commands

class Error_Handling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#@clr.error
#async def clr_error(ctx, error):
#    if isinstance(error, commands.errors.MissingPermissions):
#        pass
#    else:
#        await ctx.send("Fajne! Ale skús to ešte raz a spomeň aj nejaké konkrétne číslo.")



def setup(bot):
    bot.add_cog(Error_Handling(bot))
