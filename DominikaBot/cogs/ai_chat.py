import discord
from discord.ext import commands
import google.generativeai as genai
import os

class AIChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.key_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "gemini_key.txt")
        self.chat_sessions = {}
        
        try:
            with open(self.key_path, "r") as f:
                api_key = f.read().strip()
            
            genai.configure(api_key=api_key)
            
            self.model = genai.GenerativeModel(
                model_name='gemini-flash-lite-latest',
                system_instruction="Voláš sa Dominika. Si milá, vtipná a nápomocná asistentka na tomto Discord serveri. Odpovedaj priateľsky."
            )
        except FileNotFoundError:
            print(f"Chyba: Súbor {self.key_path} nebol nájdený!")

    def get_chat_session(self, user_id):
        if user_id not in self.chat_sessions:
            self.chat_sessions[user_id] = self.model.start_chat(history=[])
        return self.chat_sessions[user_id]

    @commands.command(name="ask")
    async def ask(self, ctx, *, otazka):
        async with ctx.typing():
            try:
                chat = self.get_chat_session(ctx.author.id)
                response = chat.send_message(otazka)
                
                odpoved = response.text
                if len(odpoved) > 2000:
                    for i in range(0, len(odpoved), 2000):
                        await ctx.send(odpoved[i:i+2000])
                else:
                    await ctx.send(odpoved)
            except Exception as e:
                print(f"DEBUG ERROR: {e}")
                await ctx.send(f"Chyba: Model nebol nájdený alebo API nie je dostupné. Skús reštartovať bota.")

    @commands.command(name="reset")
    async def reset(self, ctx):
        if ctx.author.id in self.chat_sessions:
            del self.chat_sessions[ctx.author.id]
            await ctx.send("Tvoja konverzácia s Dominikou bola vymazaná.")
        else:
            await ctx.send("Nemáš aktívnu žiadnu konverzáciu.")

async def setup(bot):
    await bot.add_cog(AIChat(bot))