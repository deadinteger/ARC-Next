import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '[]')

def read_token():
    with open("token","r") as file:
        lineRead = file.readlines()
        return lineRead[0].strip()

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 150664563124207617:
        client.load_extension(f'cogs.{extension}')
        print(f'{extension} has been loaded')
    else:
        await ctx.send("Sorry only Aster can use this.")


@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 150664563124207617:
        client.unload_extension(f'cogs.{extension}')
        print(f'{extension} has been unloaded')
        await ctx.send(f'{extension} has been unloaded')
    else:
        await ctx.send("Sorry only Aster can use this.")


@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 150664563124207617:
        client.reload_extension(f'cogs.{extension}')
        print(f'{extension} has been reloaded')
        await ctx.send(f'{extension} has been reloaded')
    else:
        await ctx.send("Sorry only Aster can use this.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename} has been loaded')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Cocaine Toenails"))

print(discord.__version__)
print(discord.version_info)
client.run(read_token())
