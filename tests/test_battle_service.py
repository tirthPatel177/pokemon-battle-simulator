import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.pokemon import Pokemon
from app.models.battle import Battle, BattleStatus
from app.services.battle_service import BattleService
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
    test_db.query(Battle).delete()
    test_db.query(Pokemon).delete()
    test_db.commit()

def test_create_battle(test_db):
    pokemon_a = Pokemon(
        name="Charmander",
        type1="fire",
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
    )
    pokemon_b = Pokemon(
        name="Squirtle",
        type1="water",
        attack=48,
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
    )
    test_db.add(pokemon_a)
    test_db.add(pokemon_b)
    test_db.commit()

    battle_service = BattleService(test_db)
    new_battle = battle_service.create_battle(pokemon_a, pokemon_b)
    assert new_battle.pokemon_a_id == pokemon_a.id
    assert new_battle.pokemon_b_id == pokemon_b.id

def test_run_battle(test_db):
    pokemon_a = Pokemon(
        name="Charmander",
        type1="fire",
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
    )
    pokemon_b = Pokemon(
        name="Squirtle",
        type1="water",
        attack=48,
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
    )
    test_db.add(pokemon_a)
    test_db.add(pokemon_b)
    test_db.commit()

    battle_service = BattleService(test_db)
    new_battle = battle_service.create_battle(pokemon_a, pokemon_b)
    test_db.refresh(new_battle)

    battle_service.run_battle(new_battle.id)
    updated_battle = test_db.query(Battle).filter(Battle.id == new_battle.id).first()
    assert updated_battle.status == BattleStatus.COMPLETED
