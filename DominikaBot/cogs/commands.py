import discord
import asyncio
import random
import sys
import contextlib

from io import StringIO
from discord.ext import commands
from random import choice


class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['Povedz,']) #Bot will send 1 random message from the list below after being triggered
    async def _8ball(self, ctx, *, question):
        filename = "./speech/yes_no.txt"
        f = open(filename,"r",encoding="utf8")
        content = f.readlines()
        await ctx.send(random.choice(content))

    @commands.command(aliases=['zmaz','zmaž','Zmaž']) #Deleting messages in channel
    @commands.has_permissions(manage_messages=True)
    async def clr(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount + 1)

    @commands.command() #Command decorator
    async def ping(self, ctx):
        await ctx.send(f'Pong!')
        await asyncio.sleep(self.bot.latency )
        await ctx.send(f' Haha to je vtip, ktorý ti dôjde asi za {round(self.bot.latency * 1000)} milisekúnd.')

  
    @commands.command()
    @commands.has_any_role('Simp')
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)


    @commands.command() # <3 Embed messages
    async def dis(self, ctx):
        embed = discord.Embed(
            title = 'Title',
            description = 'Description',
            
            colour = discord.Colour.red()
        )

        embed.set_footer(text='Footer lmao')
        embed.set_image(url='https://cdn.discordapp.com/attachments/783036978127175680/783416344393154610/dominika_portrait_.png')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/783036978127175680/783416344393154610/dominika_portrait_.png')
        embed.set_author(name='Big Rajko', icon_url = 'https://cdn.discordapp.com/attachments/783036978127175680/783416344393154610/dominika_portrait_.png')
        embed.add_field(name='Field name',value='Field Value', inline=False)
        embed.add_field(name='Field name',value='Field Value', inline=True)
        embed.add_field(name='Field name',value='Field Value', inline=True)

        await ctx.send(embed=embed)


    @commands.command(aliases=['zvelič','zvelic','stupid','matus','Matúš','Zvelič'])
    async def vyspongebobuj(self, ctx, *, message):
        try:
            await ctx.send(''.join(choice((str.upper, str.lower))(c) for c in message))
        except Exception as e: print(e)



    @commands.has_any_role('Python executor')
    @commands.command(aliases=['exec','python','run','Spusti','Spythonuj','spusti'])
    async def Spracuj(self, ctx, *, message): #TODO: rename trigger command
        reading = False
        result = []
        for line in message.split('\n'):
            if reading:
                if line.startswith('```'):
                    reading = False
                    break
                else:
                    result.append(line)
            else:
                if line.startswith('```'):
                    reading = True

        code = '\n'.join(result)


        with stdoutIO() as s:
            try:
                exec(code, globals())
                await ctx.send(s.getvalue())
            except Exception as e:
                 e = str(e) + " "
                 if ("send an empty message" in e):
                     if (s.getvalue() == '' or s.getvalue() == ' '):
                         filename = "./speech/done.txt"
                         f = open(filename,"r",encoding="utf8")
                         content = f.readlines()
                         await ctx.send(random.choice(content))
                 else:
                     await ctx.send(e)             


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

          
def setup(bot):
    bot.add_cog(Commands(bot))
