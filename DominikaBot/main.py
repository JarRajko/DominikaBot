import discord 
import os
import asyncio
from discord.ext import commands

discord.utils.setup_logging()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = 'Dominika? ', intents = intents)

@bot.event
async def on_ready():
    print("Dominika is online.")
    print('Logged in as ---->', bot.user)
    print('ID:', bot.user.id)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" you!"))

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded: {extension}')

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded: {extension}')

async def main():
    async with bot:
        if os.path.exists('./cogs'):
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    try:
                        await bot.load_extension(f'cogs.{filename[:-3]}')
                        print(f"Loaded extension: {filename}")
                    except Exception as e:
                        print(f"Failed to load extension {filename}: {e}")

        try:
            with open("token.txt", "r", encoding="utf8") as f:
                token = f.read().strip()
            await bot.start(token)
        except FileNotFoundError:
            print("Error! token does not exists!")

if __name__ == '__main__':
    asyncio.run(main())