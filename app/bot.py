import discord
from discord.ext import commands
from discord import app_commands
from discord import Message
import random

class EU4Bot(commands.Bot):

    async def on_ready(self):
        # self.add_command(self.create_eu4_league)
        print(f'Logged as {self.user}')
        
    # @commands.command("create")
    # async def create_eu4_league(self, interaction: discord.Interaction):
    #     await interaction.message.channel.send("you have created category")
    #     return