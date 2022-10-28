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

        self.youtube_dl_settings = {'format': 'bestaudio', 'no-playlist': 'False'}
        self.ffmpeg_settings = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                                'options': '-vn'}

        self.vc = None

    @commands.command()
    async def play(self, ctx):

        if ctx.message.author.voice is None:
            await ctx.channel.send(f"{ctx.author.name}, firstly join to voice channel.")
            return
        channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            self.vc = await ctx.message.author.voice.channel.connect()
            await ctx.channel.send(f'Now i in {channel}')

        url = ctx.message.content[6:]
        print('sad')
        self.vc = ctx.voice_client

        with youtube_dl.YoutubeDL(self.youtube_dl_settings) as ytb_dl:
            try:
                info = ytb_dl.extract_info(url, download=False)
                link = info['formats'][0]['url']
            except Exception as e:
                await ctx.channel.send("dsadsa" + e)

        source = discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg\\ffmpeg.exe", source=link,
                                        **self.ffmpeg_settings)
        print(source)

        if self.is_playing:
            self.music_queue.append(source)
            await ctx.channel.send(f'Track ')
        else:
            self.vc.play(source)

    @commands.command()
    async def stop(self, ctx):
        pass

    @commands.command()
    async def resume(self, ctx):
        pass

    @commands.command()
    async def check_queue(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Music(bot))
