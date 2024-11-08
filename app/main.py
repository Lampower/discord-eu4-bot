import os
import discord
import discord.types
from discord.message import Message
from app.bot import EU4Bot

# -----------------------IMPORTS ABOVE-----------------------------------------

token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")

intents = discord.Intents.default()
intents.message_content = True

client = EU4Bot(intents=intents, command_prefix=prefix)


app = client.run(token)