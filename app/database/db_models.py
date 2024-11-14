from sqlalchemy import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)

    pass

class LeagueModel(Base):
    __tablename__ = "guilds"
    
    guild_id: Mapped[int]
    league_name: Mapped[str]
    

class CategoryModel(Base):
    __tablename__ = "categories"

    league_id: Mapped[int] = mapped_column(ForeignKey('guilds.id'))
    
class ChanneModel(Base):
    __tablename__ = "channels"

    category_id: Mapped[int] = mapped_column(ForeignKey("channels.id"))

class RoleModel(Base):
    __tablename__ = "roles"
    