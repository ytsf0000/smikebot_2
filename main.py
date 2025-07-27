# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()


@bot.tree.command(name="say", description="Makes the bot say something.")
@app_commands.describe(message="The message you want the bot to say.")
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message("sending message...", ephemeral=True)
    channel_id = interaction.channel_id
    channel = bot.get_channel(channel_id)
    await channel.send(message)


@bot.tree.command(name="test")
@app_commands.describe(msg = "hello")
async def test(interaction: discord.Interaction, msg: str):
    await interaction.response.send_message(msg)


@bot.tree.command(name='grok_is_this_true')
async def grok_is_this_true(interaction: discord.Interaction):
    prob = random.random()
    if prob < 0.45:
        await interaction.response.send_message('yes')
    elif prob < 0.9:
        await interaction.response.send_message('no')
    else:
        await interaction.response.send_message('crap off')


bot.run(TOKEN)
