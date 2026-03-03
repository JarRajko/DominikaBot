import discord
from discord.ext import tasks, commands
import datetime
from zoneinfo import ZoneInfo
import os

TARGET_TIME = datetime.time(hour=12, minute=30, second=0, tzinfo=ZoneInfo("Europe/Bratislava"))

class MessageScheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_message.start()

    def cog_unload(self):
        self.daily_message.cancel()

    def get_names_by_date(self, filename, day, month):
        try:
            target_day = str(int(day))
            target_month = str(int(month))
            
            current_dir = os.path.dirname(os.path.abspath(__file__))
            root_dir = os.path.dirname(current_dir)
            full_path = os.path.join(root_dir, filename)

            if not os.path.exists(full_path):
                full_path = os.path.join(current_dir, filename)

            with open(full_path, 'r', encoding='utf-8-sig') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    
                    parts = [p.strip() for p in line.split('.')]
                    
                    if len(parts) >= 3:
                        if str(int(parts[0])) == target_day and str(int(parts[1])) == target_month:
                            names_list = parts[2:]
                            return ", ".join(names_list)
            return "Neznáme"
        except Exception as e:
            print(f"Chyba pri čítaní {filename}: {e}")
            return "Chyba"

    @tasks.loop(time=TARGET_TIME)
    async def daily_message(self):
        channel = self.bot.get_channel(715513660281454623)
        channel2 = self.bot.get_channel(1478340273820930149)
        
        if not channel:
            return

        try:
            now = datetime.datetime.now(ZoneInfo("Europe/Bratislava"))
            d, m, y = now.day, now.month, now.year
            
            sk_today = self.get_names_by_date("mena.txt", d, m)
            cz_today = self.get_names_by_date("menaCz.txt", d, m)

            days_sk = {
                'Monday': 'Pondelok', 'Tuesday': 'Utorok', 'Wednesday': 'Streda',
                'Thursday': 'Štvrtok', 'Friday': 'Piatok', 'Saturday': 'Sobota', 'Sunday': 'Nedeľa'
            }
            day_name_sk = days_sk.get(now.strftime("%A"), "Neznámy")

            embed = discord.Embed(
                title='📅 Kalendárny prehľad',
                colour=discord.Colour.dark_orange()
            )
            embed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.ymVUU-t5_o2xlgHfz1PtlQHaFP%26pid%3DApi&f=1')
            
            embed.add_field(name='Dátum', value=f"{d}.{m}.{y}", inline=True)
            embed.add_field(name='Deň', value=day_name_sk, inline=True)
            embed.add_field(name='\u200b', value='\u200b', inline=False)
            
            embed.add_field(name='🇸🇰 Meniny dnes', value=sk_today, inline=True)
            embed.add_field(name='\u200b', value='\u200b', inline=False)
            
            embed.add_field(name='🇨🇿 Svátek dnes', value=cz_today, inline=True)

            await channel.send(embed=embed)
            await channel2.send(embed=embed)
            
        except Exception as e:
            print(f"Chyba: {e}")

    @daily_message.before_loop
    async def before_daily_message(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(MessageScheduler(bot))