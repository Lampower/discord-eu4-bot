from sqlalchemy import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)

    pass

class LeagueModel(Base):
    __tablename__ = "guilds"
    guild_id = Column(Integer)
    league_name = Column(String)
    

class CategoryModel(Base):
    __tablename__ = "categories"
    league_id = Column(Integer, ForeignKey('guilds.id'))
    
class ChanneModel(Base):
    __tablename__ = "channels"
    category_id = Column(Integer, ForeignKey("channels.id"))

class RoleModel(Base):
    __tablename__ = "roles"
    