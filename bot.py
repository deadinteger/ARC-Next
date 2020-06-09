import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '[]')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} has been loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'{extension} has been unloaded')
    ctx.send(f'{extension} has been unloaded')

@client.command()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    print(f'{extension} has been reloaded')
    ctx.send(f'{extension} has been reloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename} has been loaded')


client.run('NDY2MDMzNDIwMTIwODgzMjAx.XtlxTg.BhpYfIZrMk4syeDOYw9NEYtqUA0')
