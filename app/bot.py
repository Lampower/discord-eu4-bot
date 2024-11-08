import discord
from discord.ext import commands
from discord import app_commands
from discord import Message
import random

class EU4Bot(commands.Bot):

    async def on_ready(self):
        print(f'Logged as {self.user}')
    
    async def on_message(self, message: Message):
        if (message.author == self.user):
            return
        
        if (message.content.lower().startswith("hello")):
            emoji = self.emojis[random.randint(0, len(self.emojis)-1)]
            await message.add_reaction(emoji)
            await message.channel.send(f"Hi {message.author}")
        

    async def create_eu4_league(self, interaction: discord.Interaction):
        return