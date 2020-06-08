import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('ARC-Next is ready')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name = 'rose')
        await member.add_roles(role)
        print(f'{member} has joined the server')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server')
        

def setup(client):
    client.add_cog(Events(client))
