from .bot import EU4Bot
from discord import *
from discord.ext import commands
from discord.ext.commands import Context, has_permissions

import app.configs.en_conf as t

class EU4ChatCommands(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.add_commands()

    @commands.command(name="setting")
    @has_permissions(administrator=True)
    async def settings(ctx: Context):
        raise NotImplementedError()

    @commands.command(name="create")
    async def create_league(ctx: Context):
        await self.send_message(ctx, t.CREATE_LEAGUE)
        return 

    async def send_message(self, ctx: Context, msg: str):
        await ctx.channel.send(msg)

    # create category with league name 
    async def create_category(self,ctx: Context, category_name: str) -> CategoryChannel:
        guild = ctx.channel.guild
        # adding it to db?
        return await guild.create_category(category_name)

    # create channels in category
    async def create_channel(self, category: CategoryChannel, channel_name: str) -> TextChannel:
        return await category.create_text_channel(channel_name)

    # no need in this but still
    async def set_permissions_in_channel(self, channel: TextChannel, roles: Role):
        await channel.set_permissions(roles)

    # create role for category to be able to write there and see what is going on
    # create admin role for managing this category
    async def create_role(self, ctx: Context, role_name: str) -> Role:
        guild = ctx.channel.guild
        role = await guild.create_role(name=role_name)

    def run(self) -> None:
        self.bot.run(self.token)