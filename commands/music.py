import discord
import ffmpeg
from discord.ext import commands


class Music(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx):
        if ctx.author.voice is None:
            await ctx.channel.send(f"{ctx.author.name}, firstly join to voice channel.")
            return
        channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await channel.connect()
        else:
            await ctx.voice_client.move_to(channel)
        url = ctx.message.content[5:]


    @commands.command()
    async def disconnect(self, ctx):
        if ctx.voice_client is None:
            await ctx.channel.send("Firstly i need to join to voice channel.")
            return
        await ctx.voice_client.disconnect()

    @commands.command()
    async def test(self, ctx):
        print(ctx.voice_client.channel)
        print(dir(ctx.voice_client.channel))


def setup(bot):
    bot.add_cog(Music(bot))
