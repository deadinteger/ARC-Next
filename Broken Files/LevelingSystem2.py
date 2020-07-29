
import discord
import json
import os
from discord.ext import commands


class LevelingSystem2(commands.Cog):

    def __init__(self,client):
        self.client = client

    os.chdir(r'C:\Users\SORA_\OneDrive\Desktop\PyBot\ARC-Next\cogs')

    @commands.Cog.listener()
    async def on_message(self, message):
        print("Message Sent")
        with open('../users.json', 'r') as f:
            users = json.load(f)

        for key in users.keys():
            print(message.author.id)
            if int(key) != user.id:
                #print(user.id)
                users[message.author.id] = {}
                users[message.author.id]['experience'] = 0
                users[message.author.id]['level'] = 1
        users[message.author.id]['experience'] += 5

        with open('../users.json', 'w') as f:
            json.dump(users,f)


def setup(client):
    client.add_cog(LevelingSystem2(client))
