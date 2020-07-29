import random
import requests
import pprint
import json
import os
from discord.ext import commands


class DnDNode(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def newdndserver(self,ctx):
        server = ctx.guild.id
        members = ctx.guild.members
        if f'{server}'.isdir() & f'{server}.exists()':
            ctx.send("Server already exists")
        else:
            os.makedirs(f'{server}')
            for member in members:
                os.makedirs(f'{server}/{member.id}')


def setup(client):
    client.add_cog(DnDNode(client))
