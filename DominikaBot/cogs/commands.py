import discord
import asyncio
import random

from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['Povedz,']) #Bot will send 1 random message from the list below after being triggered
    async def _8ball(self, ctx, *, question):
        responses = ['Áno.',
                     'Nie.',
                     'Je to možné.',
                     'Je to veľmi pravdepodobné.',
                     'Akoby sa stalo.',
                     'Ani náhodou.',
                     'Určite.',
                     'Nebuď smiešny.',
                     'To ti teraz neviem povedať.',
                     'Pochybujem o tom.',
                     'Môžeš sa nato spoľahnúť.',
                     'Jedného dňa určite.',
                     'Je to veľmi nejasné.',
                     'S tým by som veľmi nepočítala.',
                     'Skôr áno než nie.',
                     'Nie je to isté.',
                     'Neviem vôbec.',
                     'Ťažká otázka.',
                     'Raz tomu tak bude.',
                     'Nepýtaj sa ma také kraviny.',
                     'Prečo ťa zaujíma, čo si myslím?',
                     'Istotne.',
                     'Istotne nie.',
                     'Pravdepodobne.',
                     'Sústreď sa a spýtaj sa znova lebo ti nie je rozumieť.']
        await ctx.send(f'{random.choice(responses)} ')

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

    #@commands.command(aliases=['Kde sme?'])
    #async def server_id(self, ctx, *, message):
    #    await ctx.send(ctx.)


          
def setup(bot):
    bot.add_cog(Commands(bot))
