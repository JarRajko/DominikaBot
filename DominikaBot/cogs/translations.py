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
        await ctx.send("word is " + word)
        await ctx.send("lang is " + lang)
        print (dictionary.translate("Range",'es'))
        await ctx.send(print (dictionary.translate("Range",'es')))
        await ctx.send(dictionary.translate(word,lang))
        print(word)
        print(lang)


    @commands.command()
    async def vyznam(self, ctx, word):
        await ctx.send(', '.join(dictionary.meaning(word)))


def setup(bot):
    bot.add_cog(Translations(bot))
