import random
import requests
import pprint
import json
import os
import os.path
from discord.ext import commands


class DnDNode(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def newdndserver(self,ctx):
        server = ctx.guild.id
        members = ctx.guild.members
        if os.path.exists(f'{server}') & os.path.isdir(f'{server}'):
            await ctx.send("Server already exists")
        else:
            try:
                os.makedirs(f'{server}')
            except OSError:
                print("Path creation failed.")
                await ctx.send("Path creation failure")
            else:
                await ctx.send("Path creation success!")
            for member in members:
                try:
                    os.makedirs(f'{server}/{member.id}')
                except OSError:
                    print("Path creation failed.")
                else:
                    print("Path creation success!")

    @commands.command()
    async def spells(self, ctx):
        await ctx.send("https://donjon.bin.sh/5e/spells/")

    @commands.command()
    async def classes(self, ctx):
        await ctx.send("http://dnd5e.wikidot.com/#toc5")

    @commands.command()
    async def names(self, ctx):
        await ctx.send("https://www.fantasynamegenerators.com/")

    @commands.command()
    async def roll(self, ctx, dice):
        if dice == 4 | dice == 6 | dice == 8 | dice == 12 | dice == 20:
            await ctx.send(random.randint(1, dice))
        else:
            await ctx.send("Please use a valid 5e dice type, 4, 6, 8, 12 and 20 \n Ex: /roll 4")


def setup(client):
    client.add_cog(DnDNode(client))
