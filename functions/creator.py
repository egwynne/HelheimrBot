import discord
from datetime import datetime


def createEmbed(title, description, **kwargs):
    embed = discord.Embed(
        title=title,
        description=description,
        colour=discord.Colour.red(),
        timestamp=datetime.today(),
    )


    return embed

