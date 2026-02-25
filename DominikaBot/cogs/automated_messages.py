import discord
from discord.ext import tasks, commands
import datetime
from zoneinfo import ZoneInfo

TARGET_TIME = datetime.time(hour=12, minute=30, tzinfo=ZoneInfo("Europe/Bratislava"))

class MessageScheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_message.start()

    def cog_unload(self):
        self.daily_message.cancel()

    def get_names_by_date(self, filename, day, month):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(';')
                    if parts[0] == day and parts[1] == month:
                        return parts[2], parts[3]
            return "Neznáme", "Neznáme"
        except Exception:
            return "Chyba pri čítaní", "Chyba pri čítaní"

    @tasks.loop(time=TARGET_TIME)
    async def daily_message(self):
        channel = self.bot.get_channel(796007842929836042)
        channel = self.bot.get_channel(715513660281454623)
        if not channel:
            return

        try:
            now = datetime.datetime.now(ZoneInfo("Europe/Bratislava"))
            year = str(now.year)
            day = str(now.day)
            month = str(now.month)
            
            sk_today, sk_tomorrow = self.get_names_by_date("mena.txt", day, month)
            cz_today, cz_tomorrow = self.get_names_by_date("menaCz.txt", day, month)

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
            
            embed.add_field(name='Dátum', value=f"{day}.{month}.{year}", inline=True)
            embed.add_field(name='Deň', value=day_name_sk, inline=True)
            embed.add_field(name='\u200b', value='\u200b', inline=False)
            
            embed.add_field(name='🇸🇰 Meniny dnes', value=sk_today, inline=True)
            embed.add_field(name='\u200b', value='\u200b', inline=False)
            
            embed.add_field(name='🇨🇿 Svátek dnes', value=cz_today, inline=True)

            await channel.send(embed=embed)
            
        except Exception as e:
            print(f"Chyba v automatickom odosielaní: {e}")

    @daily_message.before_loop
    async def before_daily_message(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(MessageScheduler(bot))