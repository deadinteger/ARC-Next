import discord
from discord.ext import commands


class LivingPuppet(commands.Cog):

    def __init__(self, client):
        self.client = client
#
    @commands.command()
    async def repeat(self, ctx): 
        if ctx.author.id == 150664563124207617:
            channel = self.client.get_channel(666377986324299779)
            await channel.send(ctx.message.content[9:100])

def setup(client):
    client.add_cog(LivingPuppet(client))
