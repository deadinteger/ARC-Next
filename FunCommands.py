import discord
import random
import requests
from discord.ext import commands

class FunCommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self,ctx, *,question):
        responses =['It is certain',
                    'Maybe',
                    'Maybe Not',
                    'Most Likely',
                    'Nope',
                    'Yes',
                    'Sure']
        await ctx.send(f'Question {question}\n Answer: {random.choice(responses)}')


    @commands.command()
    async def catpls(self,ctx):
        url = 'https://api.thecatapi.com/v1/images/search?format=json'
        headers = {
                    'Content-Type': 'application/json',
                    'x-api-key': '17d94b92-754f-46eb-99a0-65be65b5d18f'
        }
        response = requests.request('GET', url, headers = headers)
        await ctx.send(response.json()[''])
def setup(client):
    client.add_cog(FunCommands(client))
