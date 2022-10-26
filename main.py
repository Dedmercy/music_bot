import discord
import logging
import os
from discord.ext import commands

# logging
logging.basicConfig(level=logging.INFO)


class Client(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot ready")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.channel.send(error)


# Intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

# bot prefix
bot = commands.Bot(command_prefix="!", intents=intents)

if __name__ == "__main__":
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            bot.load_extension(f'commands.{filename[:-3]}')
    bot.add_cog(Client(bot))
    bot.run('MTAzNDk3MTY1NTc5NTEzMDM5OA.Glww1S.BlaELahcZXpsefUE-Gn5-VZ5by_5h8Ahdu8ckE')
