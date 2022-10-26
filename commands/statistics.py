import discord
from discord.ext import commands


class Statistics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def amount(self, cxt):
        pass


def setup(bot):
    bot.add_cog(Statistics(bot))
