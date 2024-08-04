# tests/test_pokemon_api.py

from fastapi.testclient import TestClient
from app.main import app
from app.db.database import Base, engine
import pytest

client = TestClient(app)

@pytest.fixture(scope='module', autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_pokemon():
    response = client.post("/api/v1/pokemon/", json={
        "name": "Pikachu",
        "type1": "electric",
        "attack": 55,
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
    assert response.json()["name"] == "Pikachu"

def test_get_pokemon():
    response = client.get("/api/v1/pokemon/Pikachu")
    assert response.status_code == 200
    assert response.json()["name"] == "Pikachu"
