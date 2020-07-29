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
            ctx.send("Server already exists")
        else:
            try:
                os.makedirs(f'{server}')
            except OSError:
                print("Path creation failed.")
                ctx.send("Path creation failure")
            else:
                ctx.send("Path creation success!")
            for member in members:
                try:
                    os.makedirs(f'{server}/{member.id}')
                except OSError:
                    print("Path creation failed.")
                else:
                    print("Path creation success!")


def setup(client):
    client.add_cog(DnDNode(client))
