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

    
    @commands.command(aliases=['Povedz,','povedz','povedz ','Povedz']) #Bot will send 1 random message from the list below after being triggered
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
            title = 'Ping',
            description = 'Príkaz na zistenei odozvy. Čisto informatívny.',
            
            colour = discord.Colour.red()
        )

        #embed.set_image(url='https://cdn.discordapp.com/attachments/783036978127175680/783416344393154610/dominika_portrait_.png')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/783036978127175680/783416344393154610/dominika_portrait_.png')
        #embed.set_author(name='Big Rajko', icon_url = 'https://cdn.discordapp.com/attachments/783036978127175680/783416344393154610/dominika_portrait_.png')
        embed.add_field(name='Požiadavky',value='Žiadne', inline=False)
        embed.add_field(name='Použitie',value='Dominika? ping', inline=False)
        embed.add_field(name='Vyvíjané',value='❌', inline=False)
        embed.set_footer(text='Here comes the trivia?')

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


    
    @commands.command()
    async def ocen(self, ctx, member : discord.Member, ocenenie, description, image_url):
        
        embed = discord.Embed (
        title = ocenenie,
        description = description,
            
        colour = discord.Colour.red()
        )

        embed.set_footer(text='Ocenenie udelené od sekretárky Dominiky')
        embed.set_image(url=image_url)
        embed.set_author(name=member.display_name, icon_url = member.avatar_url)

        await ctx.message.delete()
        await ctx.send(embed=embed)


    @commands.command(aliases=['poke','stuchni','píchni'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def pichni(self, ctx, member : discord.Member = None):
        try:
            if member is not None:
                channel = member.dm_channel
                if channel is None:
                    channel = await member.create_dm()
                filename = "./speech/pokes.txt"
                f = open(filename,"r",encoding="utf8")
                content = f.readlines()
                
                filename2 = "./speech/done.txt"
                f2 = open(filename2,"r",encoding="utf8")
                content2 = f2.readlines()
                f.close()
                f2.close()
                await ctx.send(random.choice(content2))  
                await channel.send("%s"% ctx.author.name + " " + random.choice(content))
            else:
                await ctx.send("Použi @mention ak chceš niekoho štuchnúť.")
        except Exception as e:
            print(e)
            await ctx.send("Pekny pokus.")


    @commands.command(aliases=["odkáž","odkaz","Odkáž","Odkáž "])
    @commands.cooldown(1,10,commands.BucketType.user)
    async def tell(self, ctx, message, member : discord.Member = None ):
        try:
            if member is not None:
                channel = member.dm_channel
                if channel is None:
                    channel = await member.create_dm()

                filename2 = "./speech/tell.txt"
                f2 = open(filename2,"r",encoding="utf8")
                content2 = f2.readlines()
                f2.close()
                await ctx.send(random.choice(content2))  
                await channel.send("%s"% ctx.author.name + " ti odkazuje, citujem: \" " + message + " \"")
            else:
                await ctx.send("Komu ale?")
        except Exception as e:
            print(e)
            await ctx.send("Pekny pokus.")


    @commands.command(aliases=['hod','diceroll'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hod_kockou(self, ctx):
        kocka1 =            "```  ____\n /\\' .\\ \n/: \\___\\\n\\' / . /\n \\/___/ \n```"

        kocka2 =         "```  _____\n / .  /\\\n/____/..\\\n\\'  '\\  /\n \\'__'\\/\n```"

        msg = await ctx.send(kocka1)  
        for i in range (5):
            await asyncio.sleep(0.1)
            await msg.edit(content = kocka2)
            await asyncio.sleep(0.1)
            await msg.edit(content = kocka1)
        await msg.edit(content = "```\n.\n.\n.Tvoje cislo je " + str(random.randint(1,6))+" \n.\n.```")
        #edit_message(msg,"Hadzem kockou.....")


    @commands.command(aliases=["plus rep", "+ rep"])
    async def plus_rep(self, ctx, member:discord.Member = None):
         if member is not None:
            f = open("./reputation.txt","w",encoding="utf8")
            content = f.readlines()
            content = content.split("\n")
            await ctx.send(content)
            
            for i in content:
                await ctx.send(i)
            f.close()
            await ctx.send(member)
         else:
             await ctx.send("Ešte raz, komu to ten + rep?")
    
    @commands.command()
    async def ban(self, ctx, member : discord.Member = None):
        if member is not None:
            await ctx.send("https://media1.tenor.com/images/d856e0e0055af0d726ed9e472a3e9737/tenor.gif")
            await ctx.send("<@" + str(member.id) + "> má ban!!§")
        else:
            await ctx.send("Použi @mention pre banan.")
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandNotFound):
            filename = "./speech/unknown_command.txt"
            f = open(filename,"r",encoding="utf8")
            content = f.readlines()
            await ctx.send(random.choice(content))
        else:
            await ctx.send(error)




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
