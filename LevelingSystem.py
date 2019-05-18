'''
import discord
import json
import os
from discord.ext import commands


class LevelingSystem(commands.Cog):

    def __init__(self,client):
        self.client = client

    os.chdir(r'C:\Users\Kristian\Documents\GitHub\ARC-Next')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('users.json','r') as f:
            users = json.load(f)

        await update_data(self, users, member)

        with open('users.json','w') as f:
            json.dump(users,f)

    @commands.Cog.listener()
    async def on_message(self, message):
        print("Message Sent")
        with open('users.json','r') as f:
            users = json.load(f)

        print(users)
        await update_data(self,users, message.author)
        await add_experience(self,users, message.author, 5)
        await level_up(self,users,message.author,message.channel)

        with open('users.json','w') as f:
            json.dump(users,f)


async def update_data(self,users, user):
    for key in users.keys():
        print(key)
        if int(key) != user.id:
            #print(user.id)
            users[user.id] = {}
            users[user.id]['experience'] = 0
            users[user.id]['level'] = 1


async def add_experience(self,users,user,exp):
    users[user.id]['experience'] += exp


async def level_up(self,users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int (experience ** (1/4))

    if lvl_start < lvl_end:
        await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention,lvl_end))
        users[user.id]['level'] = lvl_end

def setup(client):
    client.add_cog(LevelingSystem(client))
'''
