import discord
import random

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
            content = open_file_txt("./speech/help.txt")
            await message.author.send(str(content))
            channel = message.channel.id
            await message.channel.send('Pozri si správy ;-)')
        else:
            pass

        try:
            if (message.content[0] == "/"):
                content = open_file_txt("./speech/emotes.txt").split("\n")
                for i in range (len(content)):
                    if message.content in content[i]:
                        s = content[i].split("|")
                        await message.channel.send(s[1])
                        break
        except Exception as e: #bugfex
            pass

        if ("drz hubu" in message.content.lower() or "drž hubu" in message.content.lower() and str(message.author) != "Dominika#1684"):
             await message.channel.send("Ty drž hubu.")
        else:
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

        if (message.content == "otazka"):
            q = open_file_txt("./speech/questions.txt").split("\n")
            await message.channel.send(random.choice(q))

            
        if str(message.author) != "Dominika#1684":
            triggers = open_file_txt("./speech/triggers.txt").split("\n")
            sensitive_triggers = open_file_txt("./speech/sensitive_triggers.txt").split("\n")
            
            for i in range (len(triggers)):
                try:
                    split_triggers = triggers[i].split("|")
                    split_sensitive_triggers = sensitive_triggers[i].split("|")
                    if message.content == split_triggers[0]:
                        await message.channel.send(split_triggers[1])
                        break
                    elif split_sensitive_triggers[0] in message.content:
                        await message.channel.send(split_sensitive_triggers[1])
                except Exception as e:
                    pass

def open_file_txt(filePath):
    f = open(filePath,"r",encoding="utf8")
    content = "".join(f.readlines())
    f.close()
    return content
    

async def setup(bot):
    await bot.add_cog(On_message(bot))
