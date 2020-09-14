
import discord
import json
import os
from discord.ext import commands


class LevelingSystem(commands.Cog):

    def __init__(self,client):
        self.client = client

    os.chdir(r'C:\Users\SORA_\OneDrive\Desktop\PyBot\ARC-Next\cogs')

    


def setup(client):
    client.add_cog(LevelingSystem(client))
