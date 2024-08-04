# tests/test_pokemon_service.py

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.pokemon import Pokemon
from app.schemas.pokemon import PokemonCreate
from app.services.pokemon_service import PokemonService
from app.db.database import Base

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope='module')
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(autouse=True)
def clean_db(test_db):
    test_db.query(Pokemon).delete()
    test_db.commit()

def test_create_pokemon(test_db):
    pokemon_service = PokemonService(test_db)
    new_pokemon = pokemon_service.create_pokemon(PokemonCreate(
        name="Bulbasaur",
        type1="grass",
        type2="poison",
        attack=49,
        against_bug=1.0,
        against_dark=1.0,
        against_dragon=1.0,
        against_electric=1.0,
        against_fairy=1.0,
        against_fight=1.0,
        against_fire=1.0,
        against_flying=1.0,
        against_ghost=1.0,
        against_grass=1.0,
        against_ground=1.0,
        against_ice=1.0,
        against_normal=1.0,
        against_poison=1.0,
        against_psychic=1.0,
        against_rock=1.0,
        against_steel=1.0,
        against_water=1.0
    ))
    assert new_pokemon.name == "Bulbasaur"
    assert new_pokemon.type1 == "grass"
    assert new_pokemon.attack == 49

def test_get_pokemon_by_name(test_db):
    pokemon_service = PokemonService(test_db)
    pokemon_service.create_pokemon(PokemonCreate(
        name="Charmander",
        type1="fire",
        type2=None,
        attack=52,
        against_bug=1.0,
        against_dark=1.0,
        against_dragon=1.0,
        against_electric=1.0,
        against_fairy=1.0,
        against_fight=1.0,
        against_fire=1.0,
        against_flying=1.0,
        against_ghost=1.0,
        against_grass=1.0,
        against_ground=1.0,
        against_ice=1.0,
        against_normal=1.0,
        against_poison=1.0,
        against_psychic=1.0,
        against_rock=1.0,
        against_steel=1.0,
        against_water=1.0
    ))
    pokemon = pokemon_service.get_pokemon_by_name("Charmander")
    assert pokemon is not None
    assert pokemon.name == "Charmander"
