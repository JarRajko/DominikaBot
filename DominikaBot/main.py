import discord 
import random
import os
import json

from discord.ext import commands, tasks
from itertools import cycle


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = 'Dominika? ', intents = intents)
status = cycle(['Apex Legends','Genshin Impact','League of Legends'])
players = {}

@bot.event #Event triggered when bot is ready.. :-|
async def  on_ready():
    pass
    #change_status.start()
    #print("Bot is ready.")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    with open('data.json','r',encoding='utf8') as f:
            user = json.load(f)
    
    try:
        with open('data.json','w',encoding='utf8') as f:
            user[str(message.author.id)]['exp'] = user[str(message.author.id)]['exp']+1
            lvl_start = user[str(message.author.id)]['level']
            lvl_end = user[str(message.author.id)]['exp'] ** (1.5/4)
            if lvl_start < lvl_end:
                user[str(message.author.id)]['level'] = user[str(message.author.id)]['level']+1
                lvl = user[str(message.author.id)]['level']
                await message.channel.send(f"{message.author.name} has leveld his bugbot up to {lvl}")
                json.dump(user,f,sort_keys=True,ensure_ascii=False)
                return
            json.dump(user,f,sort_keys=True,indent=4, ensure_ascii=False)
            print("data updated")
            
    except:
        
        with open('data.json','w',encoding='utf8') as f:
            #user = {}
            user[str(message.author.id)] = {}
            user[str(message.author.id)]['level'] = 0 
            user[str(message.author.id)]['exp'] = 0
            json.dump(user,f,sort_keys=True,indent=4,ensure_ascii=False)
        print("data inserted")


@bot.event #Event triggered when someone joins the server
async def on_member_join(ctx):
    #ctx.send(f'Ahoj {member}.')
    pass

@bot.event #Event triggered when someone leaves the server no matter for what reasson.
async def on_member_remove(ctx):
    pass

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Nechapem.')
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.reactiongifs.com%2Fr%2F2013%2F08%2Fno-power.gif&f=1&nofb=1')
#@bot.command() #Checking the lattency of our bot
#async def ping(ctx): #CTX - context some sort of data obtained automatically
#    await ctx.send(f'Pong! Haha to je vtip, ktorý ti dôjde asi za {round(bot.latency * 1000)} milisekúnd.')


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
@commands.has_permissions(manage_messages=True)
async def clr(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)

@bot.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

def is_check_user(ctx): #Check user
    return ctx.author.id == 604630490225573898

@bot.command()
@commands.check(is_check_user) #Check user
async def testicek(ctx):
    await ctx.send("Yes masťer.")

@bot.command()
@commands.has_any_role('Simp')
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

    
@clr.error
async def clr_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        pass
    else:
        await ctx.send("Fajne! Ale skús to ešte raz a spomeň aj nejaké konkrétne číslo.")

for filename in os.listdir('.\cogs')    :
    if filename.endswith('.py'):
        print("Loaded extension: " + str(filename))
        bot.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(seconds=1800)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

@bot.command() # <3 Embed messages
async def dis(ctx):
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



    
bot.run('NzgzMDIwNjIwNDUwODg5NzM5.X8Uqxw.O5_xj7SuQBJtR49VFkbynsOW26c')    
