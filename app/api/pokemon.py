# app/api/pokemon.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.pokemon import PokemonCreate, PokemonRead
from app.services.pokemon_service import PokemonService
from app.db.database import get_db

router = APIRouter()

@router.post("/", response_model=PokemonRead)
def create_pokemon(pokemon: PokemonCreate, db: Session = Depends(get_db)):
    pokemon_service = PokemonService(db)
    return pokemon_service.create_pokemon(pokemon)

@router.get("/", response_model=list[PokemonRead])
def list_pokemons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pokemon_service = PokemonService(db)
    return pokemon_service.get_pokemons(skip, limit)

@router.get("/{name}", response_model=PokemonRead)
def read_pokemon_by_name(name: str, db: Session = Depends(get_db)):
    pokemon_service = PokemonService(db)
    pokemon = pokemon_service.get_pokemon_by_name(name)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemon
