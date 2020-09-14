import discord
import shutil
import os
import time
import youtube_dl
import tracemalloc
import pprint
import json
import asyncio
from youtube_search import YoutubeSearch
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from discord.ext import commands

songs = []
tracemalloc.start()
val = URLValidator()


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
    async def play(self, ctx, *, url):
        server = ctx.message.author.guild
        voice = ctx.message.author.guild.voice_client
        try:
            val(url)
            # await ctx.channel.purge(2)
            await ctx.send("Please Wait.")
            self.downloadSong(url)
            await ctx.channel.purge(limit=2)
            if voice and voice.is_playing():
                await ctx.send("Queued")
                time.sleep(15)
                await ctx.channel.purge(limit=1)
            else:
                self.playSong(voice, server)
        except ValidationError:
            # await ctx.send("Searching disabled at the moment.")
            results = YoutubeSearch(url, max_results=5).to_json()
            y = json.loads(results)
            pp = pprint.PrettyPrinter()
            searchList = ""
            listnum = 1
            songlist = []
            for x in y["videos"]:
                songlist.append((f'youtube.com{x["url_suffix"]}', f'{x["title"]}'))
                searchList += f'{listnum}:{x["title"]} \nDuration:{x["duration"]}\nChannel:{x["channel"]}\n\n'
                listnum += 1
            listnum = 1
            embed = discord.Embed(
                title='Youtube Search',
                description='Choose a video by typing 1 - 5',
                color=discord.Colour.blue()
            )
            embed.set_author(name='Arc X', icon_url='https://cdn.discordapp.com/avatars/466033420120883201/274f3c3a5e577eaaec7265dc7c00b1ef.png?size=128')
            embed.set_image(url='https://cdn.discordapp.com/avatars/466033420120883201/274f3c3a5e577eaaec7265dc7c00b1ef.png?size=128')
            embed.add_field(name='Songs', value=searchList, inline=False)
            await ctx.channel.send(embed=embed)

            def checksong(x):
                return x.author == ctx.author and x.content.isdigit()

            try:
                songchoice = (await self.client.wait_for('message', check=checksong, timeout=25.0))
                # print(songchoice.content)
                # songs.append(songlist[int(songchoice.content)][0])
                await ctx.send(f'You have chosen #{songlist[int(songchoice.content)-1][1]}, it will be queued')
                self.downloadSong(songlist[int(songchoice.content)-1][0])
                if voice and voice.is_playing():
                    await ctx.send("Queued")
                    time.sleep(15)
                    await ctx.channel.purge(limit=1)
                else:
                    self.playSong(voice, server)


            except asyncio.TimeoutError:
                return await ctx.send("Sorry, you took too long. Please use the play function again.")
            
                

        except discord.ext.commands.errors.MissingRequiredArgument:
            await ctx.send("Please enter a link or search terms")

    @commands.command()
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

    @commands.command()
    async def volume(self, ctx, vol):
        server = ctx.message.author.guild
        voice = server.voice_client
        if voice and voice.is_playing():
            # voice.source = discord.PCMVolumeTransformer(voice.source)
            newVolume = float(vol) / 100.0
            await ctx.send(f'current vol is {newVolume}')
            voice.source.volume = newVolume
        else:
            ctx.send("Please be in the VC with the bot.")

    @commands.command(pass_context=True, aliases=['skip'])
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

    # Beginning of Helper Functions

    def downloadSong(self, url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'default_search': "ytsearch",
            'noplaylist': True
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
        for file in os.listdir(os.getcwd()):
            if file.endswith('mp3'):
                shutil.move(f'{os.getcwd()}/{file}', f'{os.getcwd()}/songs/{file}')
                songs.append(file)
        # print(songs)

    def playSong(self, voice, ctx):
        try:
            currsong = songs.pop(0)
            currsong = f'{os.getcwd()}/songs/{currsong}'

            def playNext(error):
                os.remove(currsong)
                try:
                    if songs[0]:
                        self.playSong(voice, ctx)
                except IndexError:
                    print("Queue is done!")
            voice.play(discord.FFmpegPCMAudio(currsong), after=playNext)
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.05
        except AttributeError:
            print("The bot is not in a voice channel, use []join")


def setup(client):
    client.add_cog(MusicCog(client))
