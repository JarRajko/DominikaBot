import discord
import os
import random

from discord.ext import commands


class Lolko(commands.Cog):

    

    @commands.command()
    async def roztried(self, ctx, *, memberList):
        inp = memberList.split(" ")
        inp2 = list(inp)
        t1 = []
        t2 = []
                
            
        if (len(inp) < 10):
            await ctx.send("Chyba vam este " + str(10 - len(inp)))   
            pass
        elif (len(inp) > 10):
            await ctx.send("Je vas az " + str(len(inp)) + " musite vykopnut " + str(len(inp) - 10) )
            pass
        else:
              
            while("" in inp): 
                inp.remove("")

            for i in range (len(inp)):
                element = inp[i]
                if (element[0] == "+"):
                    inp2.remove(element)
                    t2.append(element[1:])
                elif (element[0] == "-"):
                    inp2.remove(element)
                    t1.append(element[1:])


            while (len(t1) != 5):
                ch = random.choice(inp2)
                inp2.remove(ch)
                t1.append(ch)

            while (len(t2) != 5):
                ch = random.choice(inp2)
                inp2.remove(ch)
                t2.append(ch)
                

            output = "```diff\n Team 1: \n\n"

            for i in t1:
                output += "- " + i + "\n"

            output += "```\n ```diff\n"
            output += " Team 2:\n\n"
            for i in t2:
                output += "+ " + i + "\n"
            output += "```"    
            await ctx.send(output)



    @commands.command(pass_context=True)
    async def emoji(self, ctx):
        msg = await ctx.send("working")
        emoji = '\N{Black Universal Recycling Symbol}'
        await msg.add_reaction(emoji)
            

    def __init__(self, bot):
        self.bot = bot
        #self.sprava = sprava

def setup(bot):
    bot.add_cog(Lolko(bot))
