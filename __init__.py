import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("Corriendo de pana.")



for filename in os.listdir('bot_commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'bot_commands.{filename[:-3]}')


bot.run(TOKEN)
