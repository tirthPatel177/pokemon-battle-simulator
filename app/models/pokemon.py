from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type1 = Column(String, index=True)
    type2 = Column(String, index=True, nullable=True)
    attack = Column(Integer)
    
    against_bug = Column(Float)
    against_dark = Column(Float)
    against_dragon = Column(Float)
    against_electric = Column(Float)
    against_fairy = Column(Float)
    against_fight = Column(Float)
    against_fire = Column(Float)
    against_flying = Column(Float)
    against_ghost = Column(Float)
    against_grass = Column(Float)
    against_ground = Column(Float)
    against_ice = Column(Float)
    against_normal = Column(Float)
    against_poison = Column(Float)
    against_psychic = Column(Float)
    against_rock = Column(Float)
    against_steel = Column(Float)
    against_water = Column(Float)