# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='test')
async def test(ctx):
    response = "test"
    await ctx.send(response)

bot.run(TOKEN)
