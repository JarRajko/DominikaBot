import discord
from PyDictionary import PyDictionary
dictionary=PyDictionary()

from discord.ext import commands

class Translations(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def synonymum(self, ctx, synonymum):
        await ctx.send("Tu su synonymá pre " + synonymum + ": ")
        await ctx.send(', '.join(dictionary.synonym(synonymum)))
        

    @commands.command()
    async def antonymum(self, ctx, anto):
        await ctx.send("Tu su antonymá pre " + anto + ": ")
        await ctx.send(', '.join(dictionary.antonym(anto)))
    
    @commands.command()
    async def preloz(self, ctx, word, lang):
        await ctx.send("```" + dictionary.translate(word,lang) + "```")


    @commands.command(aliases = ['meaning', 'Meaning', 'meanings', 'Meanings', 'explain', 'Explain','vyznamy', 'Význam', 'Významy'])
    async def vyznam(self, ctx, word):
        dic = dictionary.meaning(word)
        
        result = ''
        
        for k in dic.keys():
            result += k + ':\n'
            for m in dic[k]:
                result += word + " can be: " + m + "\n\n"
        await ctx.send("```" + result + "```")

    @antonymum.error
    async def antonymumHandler(self, ctx, error):
        await ctx.send("Žiadné antonymá pre toto slová som nenašla :(")

    @synonymum.error
    async def synonymumHandler(self, ctx, error):
        await ctx.send("Žiadné synonymá pre toto slová som nenašla :(")

    @preloz.error
    async def prelozHandler(self, ctx, error):
        await ctx.send("Nejaká chyba. :(")

    @vyznam.error
    async def vyznamHandler(self, ctx, error):
        await ctx.send("Takto to nefunguje ale :ˇ(")

def setup(bot):
    bot.add_cog(Translations(bot))
