import discord
import random
import requests
import asyncio
import shutil
import pprint
import os
import json
import youtube_dl
from discord.ext import commands


class MusicCog(commands.Cog):
    def __init__(self, client):
        self.client = client

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
        queue = []
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                print("Removed old song file")
        except PermissionError:
            print("Trying to delete song file, but it's being played")
            await ctx.send("ERROR: Music playing")
            return

        await ctx.send("Obtaining music")
        server = ctx.message.author.guild
        voice = ctx.message.author.guild.voice_client
        name = ""
        print(os.getcwd())
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
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File: {file}\n")
                os.rename(file, "song.mp3")
        try:
            voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print('done', e))
        except AttributeError:
            ctx.send("The bot is not in a voice channel, use []join")
        except discord.errors.ClientException:
            queue.append(url)
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07
        nname = name.rsplit("-", 2)
        await ctx.send(f"Playing: {nname[0]}")
        print("playing\n")

    def downloadSong(self, url):
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
