import discord
import calendar
import datetime
import asyncio

from itertools import cycle
from datetime import datetime, timedelta
from . import help_cog
from discord.ext import commands, tasks

class Calendar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        #self.loopy.start()
        #print("Loop ready i guess")


    # Pomocná funkcia na získanie mien zo súboru
    def get_names_by_date(self, file_path, day, month):
        names_today = "*"
        names_tomorrow = "*"
        
        try:
            with open(file_path, "r", encoding="utf8") as f:
                content = f.readlines()
            
            # Formátujeme zajtrajší dátum, aby sme ho vedeli nájsť
            tomorrow_date = datetime.now() + timedelta(days=1)
            t_day = str(tomorrow_date.day)
            t_month = str(tomorrow_date.month)

            for i in range(len(content)):
                parts = content[i].strip().split(".")

                
                # Hľadáme dnešné meniny
                if parts[0] == day and parts[1] == month:
                    # Dnes
                    if len(parts) == 4:
                        names_today = f"{parts[2]} a {parts[3]}"
                    elif len(parts) == 5:
                        names_today = f"{parts[2]} a {parts[3]} a {parts[4]}"
                        
                    else:
                        names_today = parts[2]
                    
                    # Zajtra (zoberieme ďalší riadok ak existuje)
                    if i + 1 < len(content):
                        next_parts = content[i+1].strip().split(".")
                        if len(next_parts) == 4:
                            names_tomorrow = f"{next_parts[2]} a {next_parts[3]}"
                        elif len(next_parts) == 5:
                            names_today = f"{next_parts[2]} a {next_parts[3]} a {next_parts[4]}"
                        else:
                            names_tomorrow = next_parts[2]
                    break
                
            return names_today, names_tomorrow
        except Exception as e:
            print(f"Chyba pri čítaní {file_path}: {e}")
            return "*", "*"

    @commands.command(aliases=['Dátum', 'dátum'])
    async def datum(self, ctx):
        try:
            now = datetime.now()
            year = str(now.year)
            day = str(now.day)
            month = str(now.month)
            
            # Získame meniny pre obe krajiny pomocou našej funkcie
            sk_today, sk_tomorrow = self.get_names_by_date("mena.txt", day, month)
            cz_today, cz_tomorrow = self.get_names_by_date("menaCz.txt", day, month)

            # Preklad dní
            days_sk = {
                'Monday': 'Pondelok', 'Tuesday': 'Utorok', 'Wednesday': 'Streda',
                'Thursday': 'Štvrtok', 'Friday': 'Piatok', 'Saturday': 'Sobota', 'Sunday': 'Nedeľa'
            }
            day_name_sk = days_sk.get(now.strftime("%A"), "Neznámy")

            # Vytvorenie Embedu
            embed = discord.Embed(
                title='📅 Kalendárny prehľad',
                colour=discord.Colour.dark_orange()
            )

            embed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.ymVUU-t5_o2xlgHfz1PtlQHaFP%26pid%3DApi&f=1')
            
            embed.add_field(name='Dátum', value=f"{day}.{month}.{year}", inline=True)
            embed.add_field(name='Deň', value=day_name_sk, inline=True)
            embed.add_field(name='\u200b', value='\u200b', inline=False) # Prázdny riadok
            
            # Slovenská sekcia
            embed.add_field(name='🇸🇰 Meniny dnes', value=sk_today, inline=True)
#           embed.add_field(name='Zajtra', value=sk_tomorrow, inline=True)
            embed.add_field(name='\u200b', value='\u200b', inline=False)
            
            # Česká sekcia
            embed.add_field(name='🇨🇿 Svátek dnes', value=cz_today, inline=True)
#           embed.add_field(name='Zítra', value=cz_tomorrow, inline=True)

            await ctx.send(embed=embed)
            
        except Exception as e:
            print(f"Chyba v príkaze datum: {e}")

    
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

 
       
async def setup(bot):
    await bot.add_cog(Calendar(bot))
