import os
import discord
from discord.message import Message
from app.bot_commands import EU4BotCommands

# -----------------------IMPORTS ABOVE-----------------------------------------

token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")

intents = discord.Intents.default()
intents.message_content = True

client = EU4BotCommands(intents=intents, prefix=prefix, token=token)


app = client.run()