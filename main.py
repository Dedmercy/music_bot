import discord
import logging
from discord.ext import commands

# logging.basicConfig(level=logging.INFO)

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    print("bot is ready")


@client.command(pass_context=True)
async def play(ctx):
    words = ctx.message.content.split()
    if len(words) > 2:
        await ctx.message.channel.send('Error. wrong command.')


@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.author.channel.send("First you need to join the voice channel")
    channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await channel.connect()
    else:
        await ctx.voice_client.move_to(channel)


@client.command(pass_context=True)
async def disconnect(ctx):
    voice = ctx.message.guild.voice_client
    if voice is None :
        await ctx.author.channel.send("First i need to join the voice channel")
    else:
        await voice.disconnect()


client.run('MTAwNDE1NzMyMjkzMjc5NzQ2MQ.GP7zii.Dq3sWTurLYuSjzzEJSUVvfEgEh2yKcnLXD92Is')
