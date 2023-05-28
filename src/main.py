import os
import config 
import asyncio

import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix=".", intents=discord.Intents.all()
)


async def main():
    for i in config.cog_files:
        await bot.load_extension(i)
    
    await bot.start(config.token)



if __name__ == "__main__":
    asyncio.run(main())