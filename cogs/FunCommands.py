import discord
import random
import requests
import pprint
import json
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
        response = requests.get(url=url,headers = headers)
        x = response.json()
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(x[0]['url'])
        y = x[0]['url']
        await ctx.send(f'Here\'s your cat picture {y}')

    @commands.command()
    async def cakeCheck(self,ctx):
        memberArray = []
        await ctx.send(f'{ctx.message.author} Accruing cake report')
        for member in ctx.guild.members:
            id = member.name
            tupMember = (id, random.randint(0, 2))
            memberArray.append(tupMember)
        await ctx.send("Here is the cake report:")
        for member in memberArray:
            #pp = pprint.PrettyPrinter(indent=4)
            #pp.pprint(member[0])
            cake = "NULL"
            if member[1] == 0:
                cake = "Not Cake"
            elif member[1] == 1:
                cake = "Cake"
            await ctx.send(f'{member[0]} is {cake}\n')
            print(f'{member[0]} is {cake}\n')
        await ctx.send('Done')

    @commands.command()
    async def dogpls(self,ctx):
        url = 'https://dog.ceo/api/breeds/image/random'
        response = requests.get(url=url)
        x = response.json()
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(x["message"])
        await ctx.send(f'Here\'s your dog picture {x["message"]}')

    @commands.command()
    async def taemail(self,ctx):
        response = requests.get("https://privatix-temp-mail-v1.p.rapidapi.com/request/domains/",
        headers={
            "X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "0ed12ef340msh2e9ae05ab59ee36p11fd0bjsn3fa84321961e"
        })

        x = response.json()
        pp = pprint.PrettyPrinter(indent = 4)
        pp.pprint(x)
        #await ctx.send()

def setup(client):
    client.add_cog(FunCommands(client))
