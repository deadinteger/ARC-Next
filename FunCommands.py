import discord
import random
import requests
import pprint
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
    async def recipe(self,ctx,query,cuisine):
        url = 'https://api.spoonacular.com/recipes/search'
        headers = {
            'Content-Type': 'application/json',
        }
        number = 10
        instructionsRequired = True
        parameters = {query, cuisine,number, instructionsRequired}
        response = requests.get(url=url, headers=headers, params=parameters)
        x = response.json()
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(x)

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
