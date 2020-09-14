import discord
from discord.ext import commands

class UserCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def assignRole(self, ctx, roleName):
        try:
            role = discord.utils.get(ctx.message.guild.roles, name = roleName)
            await ctx.message.author.add_roles(role)
            await ctx.send(f'the role {role} has been added')
        except:
            await ctx.send('That role does not exist.')

    @commands.command()
    async def removeRole(self, ctx, roleName):
        roles = ctx.message.author.roles
        for role in roles:
            if roleName == role.name:
                await ctx.message.author.remove_roles(role)
                await ctx.send(f'the role {role} has been removed')

def setup(client):
    client.add_cog(UserCommands(client))
