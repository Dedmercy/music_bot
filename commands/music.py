import discord
import ffmpeg
from discord.ext import commands
import youtube_dl


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
        self.is_paused = False

        self.music_queue = []

        self.youtube_dl_settings = {'format': 'bestaudio', 'no-playlist': 'True'}
        self.ffmpeg_settings = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                                'options': '-vn'}

        self.vc = None

    @commands.command()
    async def play(self, ctx):
        self.vc = await ctx.message.author.voice.channel.connect()

        if ctx.message.author.voice is None:
            await ctx.channel.send(f"{ctx.author.name}, firstly join to voice channel.")
            return
        channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await channel.connect()
            await ctx.channel.send(f'Now i in {channel}')

        url = ctx.message.content[6:]
        self.vc = ctx.voice_client
        print(url)
        with youtube_dl.YoutubeDL(self.youtube_dl_settings) as ytb_dl:
            try:
                info = ytb_dl.extract_info(url, download=False)
                link = info['formats'][0]['url']
                source = discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg\\ffmpeg.exe", source=link,
                                                **self.ffmpeg_settings)
                self.vc.play(source)
            except Exception as e:
                await ctx.channel.send(e)


def setup(bot):
    bot.add_cog(Music(bot))
