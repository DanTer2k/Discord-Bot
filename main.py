from ast import alias
import discord
from discord.ext import commands, tasks
from discord.utils import get
import config
from youtubesearchpython import VideosSearch
import asyncio

bot = commands.Bot(command_prefix=['.'], intents = discord.Intents.all())

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))
@bot.event
async def on_message(ctx):
    for i in range(len(config.ID_IGNORE_LIST)):
        if ctx.author.id == config.ID_IGNORE_LIST[i]:
            await ctx.delete()
            print(str(ctx.author) + ": " + ctx.content)
            return#
    if 'слава украине' in ctx.content.lower() or 'славу уронили' in ctx.content.lower() or 'слава україні' in ctx.content.lower():
        await ctx.channel.send('Героям Слава!')
        try: 
            voice_channel = ctx.author.voice.channel
            voice = await voice_channel.connect()
            voice.play(discord.FFmpegPCMAudio('./memes/1.mp3'))
            await asyncio.sleep(1.5)
            await voice.disconnect()
        except: pass
    elif 'хрю' in ctx.content.lower():
        try: 
            voice_channel = ctx.author.voice.channel
            voice = await voice_channel.connect()
            voice.play(discord.FFmpegPCMAudio('./memes/2.mp3'))
            voice.source = discord.PCMVolumeTransformer(voice.source, 0.1)
            await asyncio.sleep(9)
            voice.source = discord.PCMVolumeTransformer(voice.source, 1)
            voice.source = discord.PCMVolumeTransformer(voice.source, 2)
            voice.source = discord.PCMVolumeTransformer(voice.source, 3)
            voice.source = discord.PCMVolumeTransformer(voice.source, 4)
            voice.source = discord.PCMVolumeTransformer(voice.source, 5)
            voice.source = discord.PCMVolumeTransformer(voice.source, 6)
            voice.source = discord.PCMVolumeTransformer(voice.source, 7)
            voice.source = discord.PCMVolumeTransformer(voice.source, 8)
            voice.source = discord.PCMVolumeTransformer(voice.source, 9)
            voice.source = discord.PCMVolumeTransformer(voice.source, 10)
            await asyncio.sleep(1.5)
            await voice.disconnect()
        except: pass
    elif 'сундук' in ctx.content.lower() or 'рундук' in ctx.content.lower():
        try: 
            voice_channel = ctx.author.voice.channel
            voice = await voice_channel.connect()
            voice.play(discord.FFmpegPCMAudio('./memes/3.mp3'))
            voice.source = discord.PCMVolumeTransformer(voice.source, 0.2)
            await asyncio.sleep(5.5)
            await voice.disconnect()
        except: pass
    elif 'sui' in ctx.content.lower() or 'сыш' in ctx.content.lower() or 'шыш' in ctx.content.lower():
        try: 
            voice_channel = ctx.author.voice.channel
            voice = await voice_channel.connect()
            voice.play(discord.FFmpegPCMAudio('./memes/4.mp3'))
            voice.source = discord.PCMVolumeTransformer(voice.source, 1)
            await asyncio.sleep(1.6)
            await voice.disconnect()
        except: pass
    elif 'кибербуль' in ctx.content.lower() or 'закибербулили' in ctx.content.lower():
        try: 
            voice_channel = ctx.author.voice.channel
            voice = await voice_channel.connect()
            voice.play(discord.FFmpegPCMAudio('./memes/5.mp3'))
            voice.source = discord.PCMVolumeTransformer(voice.source, 0.1)
            await asyncio.sleep(4.8)
            await voice.disconnect()
        except: pass
    elif 'погнали' in ctx.content.lower():
        try: 
            voice_channel = ctx.author.voice.channel
            voice = await voice_channel.connect()
            voice.play(discord.FFmpegPCMAudio('./memes/6.mp3'))
            voice.source = discord.PCMVolumeTransformer(voice.source, 0.2)
            await asyncio.sleep(4.3)
            await voice.disconnect()
        except: pass
    await bot.process_commands(ctx)

@tasks.loop(hours = 6)
async def auto_clear_chat():
    message_channel = bot.get_channel(config.CLEARING_CHAT_ID)
    deleted = await message_channel.purge(limit=10000)
    print(f"Channel name: {message_channel}")
    print(f'Deleted {len(deleted)} messages')
@auto_clear_chat.before_loop
async def before():
    await bot.wait_until_ready()

@bot.command(aliases=['c', 'cls', 'clr']) #Clearing chat command
async def clear(ctx, num=10000):
    try: await ctx.message.delete()
    except: pass

    deleted = await ctx.channel.purge(limit=num)
    await ctx.channel.send(f'Deleted {len(deleted)} messages', delete_after = 3)

#@bot.command(brief="1",description = "123", aliases=['q'])
@bot.command(aliases=['rn']) #Rename all users command
async def rename(ctx, *args):
    try: await ctx.message.delete()
    except: pass

    newNick = ''
    for arg in args:
        newNick+=str(arg)+' '
    if ctx.author.id == config.HOST_ID:
        for member in ctx.guild.members:
            if member.id == config.HOST_ID:
                continue
            await member.edit(nick = newNick)

@bot.command(aliases = ['p', 'pl'])
async def play(ctx): #Connect bot to voice chat
    try: await ctx.message.delete()
    except: pass

    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    print(f"Succesfully joined the voice channel: {voice_channel.name}")

@bot.command(aliases = ['l', 'leave'])
async def disconnect(ctx):  #Disconnecting bot from the voice chat
    try: await ctx.message.delete()
    except: pass

    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        print('Left from the voice channel')
    else:
        await ctx.channel.send('Лишь бы прогнать :(', delete_after = 5)

auto_clear_chat.start()
bot.run(config.TOKEN)