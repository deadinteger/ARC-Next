
import discord
import json
import os
from discord.ext import commands


class LevelingSystem(commands.Cog):

    def __init__(self,client):
        self.client = client

    os.chdir(r'C:\Users\SORA_\OneDrive\Desktop\PyBot\ARC-Next\cogs')

    async def writeFile(data):
    	with open('./users.json','w') as fp:
    		json.dump(data,fp)

    async def readFile():
    	with open('./users.json','r') as fp:
    		return json.load(fp)

    async def addXP(users, member, exp):
        if not user.id in users:
            users[member.id] = {}
            users[member.id]['experience'] = 5
            users[member.id]['level'] = 1
        else:
            users[member.id]['experience'] += exp

    @commands.Cog.listener()
    async def on_message(message):
        users = readFile()
        await addXP(users, message.author, 5)

def setup(client):
    client.add_cog(LevelingSystem(client))
