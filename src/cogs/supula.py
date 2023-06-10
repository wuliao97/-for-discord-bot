import utils.Api as api

import discord
from discord.ext import commands


class Command(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    sp = discord.SlashCommandGroup(
        "スプラトゥーン", "Various SP Commands"
    )
    
    spmap = sp.create_subgroup(
        "マップ", "Various SP MAP Commands"
    )
    
    
    @spmap.command(name="現在の情報")
    async def sp_map_now(self, inter:discord.Interaction):
        data = api.load(api.STAGE.NOW_STAGE)
        
        info = data["results"][0]
        stage = data["results"][0]["stages"]
        
        embeds = [
            discord.Embed()
            .add_field(name="Rule", value=info["rule"]["name"],  inline=False)
            .add_field(name="Start time", value=info["start_time"])
            .add_field(name="End time", value=info["end_time"])
        ]
        
        embeds.append(
            discord.Embed(
                title=stage[0]["name"],
            ).set_thumbnail(url=stage[0]["image"])
            
        )
        
        embeds.append(
            discord.Embed(
                title=stage[1]["name"]
            ).set_thumbnail(url=stage[1]["image"])
        )
        
        await inter.response.send_message(embeds=embeds)
    

    
def setup(bot:commands.Bot):
    return bot.add_cog(Command(bot))