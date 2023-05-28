import discord
from discord.ext import commands


class Command(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    
    
def setup(bot:commands.Bot):
    return bot.add_cog(Command(bot))