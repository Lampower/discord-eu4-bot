from discord import *
from discord.ext.commands import *
from app.database.db_context import session_scope


async def create_role( ctx: Context, name: str, color: Colour = None, permissions: Permissions = None) -> Role | None:
    with session_scope() as s:
        role = await ctx.guild.create_role(name=name, color=color, permissions=permissions)
        s.add(role)
        return role
    return None

async def delete_role():
    raise NotImplementedError()
    
