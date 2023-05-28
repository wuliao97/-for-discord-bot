import discord
from discord.ext import commands


class Event(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} is ready")
    
    
    
    
    
def setup(bot:commands.Bot):
    return bot.add_cog(Event(bot))