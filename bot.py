import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '!')
extensions=['FunCommands']

@client.event
async def on_ready():
    print('ARC-Next is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension,error))

@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded. [{}]'.format(extension,error))

@client.command()
async def ping(context):
    await context.send(f'Pong! {round(client.latency * 1000)}ms')



if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
            print('{} has been loaded successfully'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension,error))
    client.run('NDY2MDMzNDIwMTIwODgzMjAx.XNilnA.eyBQLO_ki1uqIPFitVZTIB_5e58')
