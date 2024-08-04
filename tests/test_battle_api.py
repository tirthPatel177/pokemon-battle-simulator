# tests/test_battle_api.py

from fastapi.testclient import TestClient
from app.main import app
from app.db.database import Base, engine
import pytest
import time

client = TestClient(app)

@pytest.fixture(scope='module', autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_battle():
    # Create first Pokémon
    response = client.post("/api/v1/pokemon/", json={
        "name": "Bulbasaur",
        "type1": "grass",
        "type2": "poison",
        "attack": 49,
        "against_bug": 1.0,
        "against_dark": 1.0,
        "against_dragon": 1.0,
        "against_electric": 1.0,
        "against_fairy": 1.0,
        "against_fight": 1.0,
        "against_fire": 1.0,
        "against_flying": 1.0,
        "against_ghost": 1.0,
        "against_grass": 1.0,
        "against_ground": 1.0,
        "against_ice": 1.0,
        "against_normal": 1.0,
        "against_poison": 1.0,
        "against_psychic": 1.0,
        "against_rock": 1.0,
        "against_steel": 1.0,
        "against_water": 1.0
    })
    assert response.status_code == 200

    # Create second Pokémon
    response = client.post("/api/v1/pokemon/", json={
        "name": "Charmander",
        "type1": "fire",
        "attack": 52,
        "against_bug": 1.0,
        "against_dark": 1.0,
        "against_dragon": 1.0,
        "against_electric": 1.0,
        "against_fairy": 1.0,
        "against_fight": 1.0,
        "against_fire": 1.0,
        "against_flying": 1.0,
        "against_ghost": 1.0,
        "against_grass": 1.0,
        "against_ground": 1.0,
        "against_ice": 1.0,
        "against_normal": 1.0,
        "against_poison": 1.0,
        "against_psychic": 1.0,
        "against_rock": 1.0,
        "against_steel": 1.0,
        "against_water": 1.0
    })
    assert response.status_code == 200

    # Create a battle
    response = client.post("/api/v1/battle/", json={
        "pokemon_a_name": "Bulbasaur",
        "pokemon_b_name": "Charmander"
    })
    assert response.status_code == 200
    assert "id" in response.json()
    battle_id = response.json()["id"]


    # Wait for the battle to complete
    time.sleep(22)  # Wait long enough for the background task to complete

    # Get the battle result
    response = client.get(f"/api/v1/battle/{battle_id}")
    print(response.json(), "Final response")
    assert response.status_code == 200
    assert response.json()["status"] == "COMPLETED"
    assert response.json()["result"] is not None
    assert "winnerName" in response.json()["result"]
    assert "wonByMargin" in response.json()["result"]
