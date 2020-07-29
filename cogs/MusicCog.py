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
        songs = []
        await ctx.send("Obtaining music")
        server = ctx.message.author.guild
        voice = ctx.message.author.guild.voice_client
        name = ""
        self.downloadSong(url, songs)
        if songs[0] is None:
            self.playSong(voice, ctx, songs)

    @commands.command()
    async def queue(self, ctx, url, songs):
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
        for file in os.listdir('./'):
            if file.endswith('mp3'):
                shutil.move(file, "./songs")
                songs.append(file)

    def playSong(self, voice, ctx, songs):
        try:
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.07
            currsong = songs.pop(0)
            voice.play(discord.FFmpegPCMAudio(currsong), after=lambda e: os.remove(currsong))
        except AttributeError:
            ctx.send("The bot is not in a voice channel, use []join")

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
