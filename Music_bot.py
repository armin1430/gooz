import os
import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import urllib.parse, urllib.request, re
import time


bot = commands.Bot(command_prefix='.')

help_commands = """
Join commands: \n
.join\n
.betap\n
.batap\n
.bia\n
.j\n
.جوین\n
.بتپ\n
----------------------------------------------------------
Leave commands:\n
.leave\n
.lv\n
.gomsho\n
.boro\n
.siktir\n
.گمشو\n
.سیکتیر\n
.برو\n
----------------------------------------------------------
Play commands:\n
.bekhoon\n
.bekhon\n
.p\n
.pla\n
.pl\n
.begooz\n
.begoz\n
.بنواز\n
.بخون\n
.بگوز\n"""

@bot.event
async def on_ready():
    print(f'{bot.user} has Successfuly Connected !')

async def ping(ctx):
    await ctx.send(f'Bot ping: {round(bot.latency * 1000)} ms')

@bot.command(pass_context=True, aliases=['komak','کمک'])
async def _help(ctx):
    await ctx.send(help_commands)

@bot.command(pass_context=True, aliases=['batap','betap','bia','j','بتپ','جوین','gooz'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'The bot has connected to {channel}\n ')

    await ctx.send(f"joined {channel} :grinning:")


# @bot.command(aliases=['user'])
# async def on_message(message):
#     x = message.guild.members
#     for member in x:
#         print(member.id)

@bot.command(pass_context=True,aliases=['clear'])
async def delete_msg(ctx,number:int):
    deleted = await ctx.channel.purge(limit=number+2)
    msg = await ctx.send(len(deleted))
    await msg.delete()

@bot.command(pass_context=True, aliases=['بگرد','youtube','begard','بیاب','biab','yt'])
async def find(ctx, *, search):

    query_string = urllib.parse.urlencode({
        'search_query' : search
    })
    htm_content = urllib.request.urlopen(
        url='https://www.youtube.com/results?search_query=' + query_string
    )
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})',htm_content.read().decode())
    # await ctx.send('https://www.youtube.com/results?search_query=' + search_results[0] )
    print("starting:")
    print(search_results)
    print(htm_content)
    print(query_string)
    print("completed")
# https://www.youtube.com/watch?v=
# https://www.youtube.com/results?search_query=
# https://www.youtube.com/results?

@bot.command(pass_context=True,aliases=['boro','gomsho','siktir','برو','سیکتیر','گمشو','lv'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print("bot left the {channel}")
        await ctx.send(f"The bot has left The {channel} :frowning2:")
    else:
        print("i don't think i am in a voice channel")
        await ctx.send("i don't think i am in a voice channel :thinking:")


@bot.command(pass_context=True, aliases=['بخون','bekhoon','bekhon','p','بنواز','pla','pl','begooz','begoz'])
async def play(ctx, url:str):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'The bot has connected to {channel}\n ')
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played already !")
        await ctx.send("ERROR: Music Playing !")
        return
    await ctx.send("Getting everyhing ready now :slight_smile:")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])
        print(url)
    for file in os.listdir("./"):
        if file.endswith("mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"{name} has finished playing !"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.7
    name = name.rsplit("-", 2)
    await ctx.send(f"Playing: {name}")
    print("Playing\n")



@bot.command(pass_context=True, aliases=['peyet'])
async def seyed(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'The bot has connected to {channel}\n ')
    await ctx.send("!Getting everyhing ready now :slight_smile:")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
    }
    voice.play(discord.FFmpegPCMAudio("seyed.mp3"), after=lambda e: print(f"has finished playing !"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1.7


    name = name.rsplit("-", 2)
    await ctx.send(f"Playing")
    print("Playing\n")


@bot.command(pass_context=True)
async def rdd(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'The bot has connected to {channel}\n ')
    await ctx.send("Y:Getting everyhing ready now :slight_smile:")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
    }
    voice.play(discord.FFmpegPCMAudio("ridam_y1.aac"), after=lambda e: print(f"has finished playing !"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.6
    name = name.rsplit("-", 2)
    await ctx.send(f"Playing")
    print("Playing\n")

@bot.command(pass_context=True)
async def sla(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'The bot has connected to {channel}\n ')

    await ctx.send("Y:Getting everyhing ready now :slight_smile:")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
    }
    voice.play(discord.FFmpegPCMAudio("aleykom.aac"), after=lambda e: print(f"has finished playing !"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.6


    name = name.rsplit("-", 2)
    await ctx.send(f"Playing")
    print("Playing\n")

@bot.command(pass_context=True,aliases=['seyed?'])
async def syd(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'The bot has connected to {channel}\n ')
    await ctx.send("Y:Getting everyhing ready now :slight_smile:")
    voice = get(bot.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
    }
    voice.play(discord.FFmpegPCMAudio("seyed!.aac"), after=lambda e: print(f"has finished playing !"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.6
    time.sleep(4)
    voice.play(discord.FFmpegPCMAudio("seyed.mp3"), after=lambda e: print(f"has finished playing !"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 1.7


    name = name.rsplit("-", 2)
    await ctx.send(f"Playing")
    print("Playing\n")




@bot.command(name="playlist")
async def _command(ctx):
    playlist = []
    await ctx.send(f"send your playlist songs")

    # This will make sure that the response will only be registered if the following
    # conditions are met:
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await bot.wait_for("message", check=check)
    if msg.content.lower() == "http":
        await ctx.send("gooz")
        # playlist.append(msg.content)
        print("its working fine")
        print(playlist)
    else:
        await ctx.send("diz")
        print("its not working either")



# @bot.event
# async def on_message(message):
#     userinput = message.content()
#     writer = message.content.author()
#     print(" said : {userinput}")


# @client.event
# async def on_message(message):
#     gid = client.get_guild(541306130262130688)
#     channels = ["score"]
#     if message.channel in channels:

# @client.event
# async def on_join(member):
#     for channel in member.server.channels:
#         if str(channel) == "score":
#             await client.send("Welcome to Galaxy {member.mention}")

# @client.event
# async def on_message(message):
#     users = ["kirem#6507"]
#     if str(message.channel) in "general" and str(message.author) in users:
#         if message.content.find("hi") != -1:
#             await message.channel.send(f"Hey {message.author}")
# @client.event
# async def on_message(message):
#     if message.content.find("seyed") != -1:
#         await message.channel.send("bezaresh la peyet")
# @client.event
# async def on_message(message):
#     if message.content.find("som") != -1:
#         await message.channel.send("@everyone")
bot.run("NzQ5OTI0NDYxOTU1Nzc2NTYy.X0zDlA.qRMHakGZSUj3TEPdhK6MtV-IKGk")