# app/schemas/pokemon.py

from pydantic import BaseModel

class PokemonBase(BaseModel):
    name: str
    type1: str
    type2: str | None = None
    attack: int
    against_bug: float
    against_dark: float
    against_dragon: float
    against_electric: float
    against_fairy: float
    against_fight: float
    against_fire: float
    against_flying: float
    against_ghost: float
    against_grass: float
    against_ground: float
    against_ice: float
    against_normal: float
    against_poison: float
    against_psychic: float
    against_rock: float
    against_steel: float
    against_water: float

class PokemonCreate(PokemonBase):
    pass

class PokemonRead(PokemonBase):
    id: int

    class Config:
        orm_mode = True
