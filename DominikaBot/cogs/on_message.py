import discord

from discord.ext import commands

class On_message(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel.id
        #await message.channel.send('message goes here')
        if (message.content == "Dominika?"):
            await message.author.send("Chceš s niečim pomôcť? Nah, tu más dostupné príkazy. Keď tak použi pomoc *príkaz *")
            filename = "./speech/help.txt"
            f = open(filename,"r",encoding="utf8")
            content = "".join(f.readlines())
            f.close()
            await message.author.send(str(content))
            channel = message.channel.id
            await message.channel.send('Pozri si správy ;-)')
        else:
            pass

        try:
            if (message.content[0] == "/"):
                filename = "./speech/emotes.txt"
                f = open(filename,"r",encoding="utf8")
                content = "".join(f.readlines()).split("\n")

                for i in range (len(content)):
                    if message.content in content[i]:
                        s = content[i].split("|")
                        await message.channel.send(s[1])
                        break
        except Exception as e: #bugfex
            pass

        if (message.content == "/emoty"):
            await message.author.send("List emote-ov oddelený pajpov.")
            filename = "./speech/emotes.txt"
            f = open(filename,"r",encoding="utf8")
            content = "".join(f.readlines())
            f.close()
            await message.author.send(str(content))
            channel = message.channel.id
            await message.channel.send('Poslala som ti emote list do DM zlato.')
    

def setup(bot):
    bot.add_cog(On_message(bot))
