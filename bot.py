import discord
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"{client.user} 로그인 완료")

@tree.command(
    name="핑",
    description="봇 테스트"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

client.run(TOKEN)