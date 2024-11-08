import os
import discord
import discord.types
from discord.message import Message

# -----------------------IMPORTS ABOVE-----------------------------------------

token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# -----------------------VARS ABOVE-----------------------------------------

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.command
async def command_name(message: Message):
    return

app = client.run(token)