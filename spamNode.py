import discord
from discord.ext import commands
from random_word import RandomWords
r= RandomWords()

client = commands.Bot(command_prefix = '!')

@client.command()
async def spam(context):
    while True:
        await context.send(r.get_random_words())
client.run('MTUwNjY0NTYzMTI0MjA3NjE3.XPNVOQ.1zStsLsY7mgKWRqhcENGEzyZqcA')
