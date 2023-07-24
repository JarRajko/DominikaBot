import discord
import calendar
import datetime
import asyncio

from itertools import cycle
from datetime import datetime
from . import help_cog
from discord.ext import commands, tasks

class Calendar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        #self.loopy.start()
        #print("Loop ready i guess")


    @commands.command(aliases=['Dátum','dátum']) 
    async def datum(self, ctx):
        try:
            year = str(datetime.now())[:4]
            day = str(datetime.now())[8:10]
            month = str(datetime.now())[5:7]
            if (month[0] == '0'): month=month[1]
            if (day[0] == '0'): day=day[1] 
            meniny = "*"
            meninyZajtra = "*"
            
            f = open("mena.txt",encoding="utf8")
            content = f.readlines()

            
                
            for i in range (len(content)):
                x = content[i]
                x = x[:-1]
                x = x.split(".")
                
                if(x[0]==day and x[1]==month):
                    if (len(x) == 4):
                        meniny = str(x[2])+ " a " + str(x[3])
                        meninyZajtra = content[i+1]
                        meninyZajtra = meninyZajtra[:-1]
                        meninyZajtra = meninyZajtra.split(".")
                        if(len(meninyZajtra) == 4):
                            meninyZajtra = str(meninyZajtra[2]) + " a " + str(meninyZajtra[3])
                        else: meninyZajtra = meninyZajtra[2]    
                        f.close()
                        break
                    else:
                        meniny = x[2]
                        if(i != (len(content) - 1)):
                            meninyZajtra = content[i+1]
                            meninyZajtra = meninyZajtra[:-1]
                            meninyZajtra = meninyZajtra.split(".")[2]
                        f.close()
                        break
                    
            dayStr = datetime.now().strftime("%A")

            if(dayStr == 'Monday'): dayStr = 'Pondelok'
            elif(dayStr == 'Tuesday'): dayStr = 'Utorok'
            elif(dayStr == 'Wednesday'): dayStr = 'Streda'
            elif(dayStr == 'Thursday'): dayStr = 'Štvrtok'
            elif(dayStr == 'Friday'): dayStr = 'Piatok'
            elif(dayStr == 'Saturday'): dayStr = 'Sobota'
            else: dayStr = 'Nedeľa'

               
            embed = discord.Embed(
                title = 'Prehľad',
                colour = discord.Colour.dark_orange()
            )

            embed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.ymVUU-t5_o2xlgHfz1PtlQHaFP%26pid%3DApi&f=1')
            embed.add_field(name='Dátum',value=day+"."+month+"."+year, inline=False)
            embed.add_field(name='Deň',value=dayStr, inline=False)
            embed.add_field(name='Meniny má dnes',value=meniny, inline=True)
            embed.add_field(name='Zajtra',value=meninyZajtra, inline=True)


            await ctx.send(embed=embed)
        except Exception as e: print(e)

    
    @commands.command(aliases=['Meniny','meno', 'Meno']) # <3 Embed messages
    async def meniny(self, ctx, name, country = 'sk'):
        try:
            
            if  (country == "cz"): f = open("menaCz.txt",encoding="utf8")
            else: f = open("mena.txt",encoding="utf8")
            content = f.readlines()
            if("." in name):
                for x in content:
                    x = x[:-1]
                    x = x.split(".")
   
                    if(str(x[0]) + "." + str(x[1]) == name):
                        await ctx.send(str(name) + " má meniny " + x[2])
                        if(len(x) == 4):
                            await ctx.send("a " + str(x[3]))
                        return
                await ctx.send("Takto to nefunguje zlato. ")
                await asyncio.sleep(1)
                await ctx.send("Nemôžeš písať random bodky a čakať že to bude v \"pohode\".");
                await asyncio.sleep(1)
                await ctx.send("Pozri si radšej ako funguje tento príkaz.")
                await asyncio.sleep(1)
                await help_cog.Help_cog(self).pomoc(self, ctx, "meniny") 
            else:
                for x in content:
                    x = x[:-1]
                    x = x.split(".")
                    if(len(x) == 4):
                        if(x[3] == name):
                            await ctx.send(name + " má meniny "+ str(x[0])+"."+str(x[1]))
                            return
                    if(x[2]==name): 
                        await ctx.send(name + " má meniny "+ str(x[0])+"."+str(x[1]))
                        return
                await ctx.send("Takto to nefunguje zlato. ")
                await asyncio.sleep(1)
                await ctx.send("Mená začínaju veľkým písmenom.");
                await asyncio.sleep(1)
                await ctx.send("Pozri si radšej ako funguje tento príkaz.")
                await asyncio.sleep(1)
                await help_cog.Help_cog(self).pomoc(self, ctx, "meniny")    
        except Exception as e: print(e)

    @meniny.error
    async def meninyHandler(self, ctx, error):
        await ctx.send("Meniny KTO?!?!");
        await asyncio.sleep(1)
        await ctx.send("Tu máš help ty nedokončovateľ príkazov.");
        await asyncio.sleep(1)
        await help_cog.Help_cog(self).pomoc(self, ctx, "meniny")

    

    #@tasks.loop(seconds=5.0)
    #async def loopy(self):
    #    return
        
async def setup(bot):
    await bot.add_cog(Calendar(bot))
