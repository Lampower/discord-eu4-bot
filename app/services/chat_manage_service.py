from discord import *
from discord.ext.commands import *

class ChatManageCommands():
    
    def __init__(self):
        pass
    
    async def create_role(self, ctx: Context, name: str, color = None) -> Role:
        return await ctx.guild.create_role(name=name, color=color)
    
    async def create_category(self, guild: Guild, name: str = "default category name", roles: list[Role] = None) -> CategoryChannel:
        last_pos = len(guild.categories)
        return await guild.create_category(name=name, position=last_pos, overwrites=roles)
    
    async def create_channel_in_category(self, name: str, category: CategoryChannel) -> TextChannel:
        return await category.create_text_channel(name=name)
    