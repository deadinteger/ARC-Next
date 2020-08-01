import discord
from discord.ext import commands

class Administrative(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


    @commands.command()
    async def clear(self, ctx, amount =5):
        await ctx.channel.purge(limit = amount)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def scan(self, ctx, *, role: discord.Role):
        for member in ctx.message.guild.members:
            if role in member.roles:
                await ctx.send(f'{member.name} has the role {role}')

    @commands.command()
    async def protect1(self, ctx, *, role: discord.Role):
        for member in ctx.message.guild.members:
            if role not in member.roles:
                await ctx.send(f'{member.name} does not have the role {role}')
                await member.kick(reason = "Protection protocol level 1")

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def protect2(self, ctx, *, role: discord.Role):
        ctx.send('Understood.')
        for member in ctx.message.guild.members:
            if role not in member.roles:
                await ctx.send(f'{member.name} does not have the role {role}')
                await member.ban(reason = "Protection protocol level 2")


def setup(client):
    client.add_cog(Administrative(client))
