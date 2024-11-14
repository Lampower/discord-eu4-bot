from app.database.db_context import session_scope
from app.database.db_models import *
from discord import *
from discord.ext.commands import *

class DbManageCommands():
    def __init__(self):
        pass
    
    def create_role(self, role_id: int) -> int:
        with session_scope() as s:
            entity = RoleModel()
            entity.id = role_id
            s.add(entity)
            return entity.id
    
    async def create_category(self, guild: Guild, name: str = "default category name", roles: list[Role] = None) -> CategoryChannel:
        last_pos = len(guild.categories)
        return await guild.create_category(name=name, position=last_pos, overwrites=roles)
    
    async def create_channel_in_category(self, name: str, category: CategoryChannel) -> TextChannel:
        return await category.create_text_channel(name=name)
    
if __name__ == "__main__":
    pass