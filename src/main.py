import os
import config 
import utils.functions as funcs
import asyncio

import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix=".", intents=discord.Intents.all()
)


def main():
    for i in funcs.cog_files:
        bot.load_extension(i)
    
    #await bot.start(config.TOKEN)
    bot.run(config.TOKEN)


if __name__ == "__main__":
    #asyncio.run(main())
    
    main()