import discord 
import random

from github import Github
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = 'Dominika? ', intents = intents)

@bot.event #Event triggered when bot is ready.. :-|
async def  on_ready():
    print("Bot is ready.")


@bot.event #Event triggered when someone joins the server
async def on_member_join(member, ctx):
    ctx.send(f'Ahoj {member}.')

@bot.event #Event triggered when someone leaves the server no matter for what reasson.
async def on_member_remove(member):
    ctx.send(f'Maj sa {member}.')

@bot.command() #Checking the lattency of our bot
async def ping(ctx): #CTX - context some sort of data obtained automatically
    await ctx.send(f'Pong! Haha to je vtip, ktorý ti dôjde asi za {round(bot.latency * 1000)} milisekúnd.')


@bot.command(aliases=['Povedz,']) #Bot will send 1 random message from the list below after being triggered
async def _8ball(ctx, *, question):
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

@bot.command(aliases=['zmaz','zmaž','Zmaž']) #Deleting messages in channel
async def clr(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


    
bot.run('NzgzMDIwNjIwNDUwODg5NzM5.X8Uqxw.O5_xj7SuQBJtR49VFkbynsOW26c')    
