import discord
import os

from discord.ext import commands

class Help_cog(commands.Cog):

    #TODO: cooldown 10s ?
    @commands.command(aliases=['halp'])
    async def pomoc(self, ctx, command):
        try:
            filename = "./help/"+command+".txt"
            f = open(filename,"r",encoding="utf8")
            content = f.readlines()
            ct = "\n".join(content)
            ctt = ct.split("▄")
            tit = ctt[0]
            des = ctt[1]
            req = ctt[2]
            reqVal = ctt[3]
            use = ctt[4]
            useVal = ctt[5]
            dev = ctt[6]
            devVal = ctt[7]
            trivia = ctt[8]
            imgUrl = ctt[9]

            embed = discord.Embed(
            title = tit,
            description = des,
            
            colour = discord.Colour.red()
            )

            embed.add_field(name=req,value=reqVal, inline=False)
            embed.add_field(name=use,value=useVal, inline=False)
            embed.add_field(name=dev,value=devVal, inline=False)
            embed.set_thumbnail(url=imgUrl)
            embed.set_footer(text=trivia)
            
            await ctx.send(embed = embed)
            
        except Exception as e:
            s = os.listdir("./help/")
            for i in range(len(s)): 
                s[i] = str(s[i])[:-4]
            ss = "\n".join(s)
            

            embed = discord.Embed(
            title = 'Pomocník',
            description = 'Žiadne strachy, toto je help command! Pre detailnejšie vysvetlenie použi Dominika? pomoc *príkaz *',
            
            colour = discord.Colour.red()
            )

            
            embed.add_field(name='Dostupné príkazy',value=ss, inline=False)


            await ctx.send(embed=embed)


    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Help_cog(bot))
