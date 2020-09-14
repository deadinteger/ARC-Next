import discord
from discord.ext import commands


class LivingPuppet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if "150664563124207617" in ctx.content:
            channel = ctx.channel
            await channel.send("Aster has left me on living puppet mode. Try not to mention him, for he will be "
                               "gone for a couple of days. "
                               "He's okay though, don't worry. All other functionalities besides administrative "
                               "controls are still fully operational.")

    @commands.command()
    async def repeat(self, ctx): 
        if ctx.author.id == 150664563124207617:
            channel = self.client.get_channel(738177113424920607)
            await channel.send(ctx.message.content[9:100])



def setup(client):
    client.add_cog(LivingPuppet(client))
