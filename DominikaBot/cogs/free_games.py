import discord
from discord.ext import commands, tasks
import aiohttp
import datetime
import os

class free_games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db_file = os.path.join(os.getcwd(), "games.txt")
        self.sent_games = self.load_sent_games()
        self.check_epic_games.start()

    def cog_unload(self):
        self.check_epic_games.cancel()

    def load_sent_games(self):
        if not os.path.exists(self.db_file):
            return set()
        with open(self.db_file, "r") as f:
            return set(line.strip() for line in f)
    
    def save_game_id(self, game_id):
        with open(self.db_file, "a") as f:
            f.write(f"{game_id}\n")
        self.sent_games.add(game_id)
    
    @tasks.loop(minutes=60)
    async def check_epic_games(self):
        url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"
        channel_id = 1476545564677243000  

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return
                
                res = await response.json()
                games = res['data']['Catalog']['searchStore']['elements']
                channel = self.bot.get_channel(channel_id)

                if not channel:
                    return

                for game in games:
                    try:
                        title = game['title']
                        game_id = game['id']
                        price = game['price']['totalPrice']['discountPrice']
                        promotions = game.get('promotions')

                        if price == 0 and promotions and promotions.get('promotionalOffers'):
                            if game_id not in self.sent_games:
                                
                                offers = promotions['promotionalOffers'][0]['promotionalOffers']
                                end_date_str = offers[0]['endDate']
                                
                                end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                                formatted_date = end_date.strftime('%d.%m.%Y %H:%M')

                                image_url = next((img['url'] for img in game['keyImages'] if img['type'] in ['Thumbnail', 'DieselStoreFrontWide']), None)
                                slug = game.get('productSlug') or game.get('urlSlug')
                                store_url = f"https://store.epicgames.com/en-US/p/{slug}"

                                embed = discord.Embed(
                                    title=f"FREE GAME: {title}",
                                    url=store_url,
                                    description=f"Ponuka platí do: **{formatted_date}**",
                                    color=discord.Color.green(),
                                    timestamp=datetime.datetime.now()
                                )
                                if image_url:
                                    embed.set_image(url=image_url)
                                embed.set_footer(text="Epic Games Store")
                                
                                await channel.send(embed=embed)
                                self.save_game_id(game_id)
                    except (KeyError, TypeError, IndexError):
                        continue

    @check_epic_games.before_loop
    async def before_check(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(free_games(bot))