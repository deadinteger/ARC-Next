import discord
import random
import requests
import asyncio
import time
import shutil
import pprint
import os
import json
import youtube_dl
from discord.ext import commands


class MusicCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    global songs

    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        server = ctx.message.author.guild
        voice_client = server.voice_client
        await voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        await ctx.send("Obtaining music")
        server = ctx.message.author.guild
        voice = ctx.message.author.guild.voice_client
        self.downloadSong(url)
        self.playSong(voice, server)

    @commands.command()
    async def queue(self, ctx, url):
        self.downloadSong(url, songs)

    def downloadSong(self, url, songs):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
        for file in os.listdir('/'):
            if file.endswith('mp3'):
                shutil.move(f'./{file}', f'./songs/{file}')
                print(os.listdir())
                print(os.listdir("./songs"))
                songs.append(file)
        time.sleep(10)

    def playSong(self, voice, ctx):
        try:
            currsong = songs.pop(0)
            print(os.listdir("./songs"))
            currsong = f'./songs/{currsong}'
            print(f'currSong is {currsong}')
            voice.play(discord.FFmpegPCMAudio(currsong), nextSong=self.playNext(voice, ctx))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.07
            # os.remove(f'./{currsong}')
        except AttributeError:
            ctx.send("The bot is not in a voice channel, use []join")

    def playNext(self,voice,ctx):
        if songs[0]:
            self.playSong(voice, ctx)

    @commands.command
    async def pause(self, ctx):

        server = ctx.message.author.guild
        voice = server.voice_client

        if voice and voice.is_playing():
            print("Music paused")
            voice.pause()
            await ctx.send("Music paused")
        else:
            print("Music not playing failed pause")
            await ctx.send("Music not playing failed pause")

    @commands.command(pass_context=True, aliases=['r', 'res'])
    async def resume(self, ctx):

        server = ctx.message.author.guild
        voice = server.voice_client

        if voice and voice.is_paused():
            print("Resumed music")
            voice.resume()
            await ctx.send("Resumed music")
        else:
            print("Music is not paused")
            await ctx.send("Music is not paused")

    @commands.command(pass_context=True, aliases=['s', 'sto'])
    async def stop(self, ctx):

        server = ctx.message.author.guild
        voice = server.voice_client

        if voice and voice.is_playing():
            print("Music stopped")
            voice.stop()
            await ctx.send("Music stopped")
        else:
            print("No music playing failed to stop")
            await ctx.send("No music playing failed to stop")


def setup(client):
    client.add_cog(MusicCog(client))
