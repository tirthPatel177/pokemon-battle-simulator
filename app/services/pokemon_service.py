from sqlalchemy.orm import Session
from app.models.pokemon import Pokemon
from app.schemas.pokemon import PokemonCreate
import Levenshtein

class PokemonService:
    def __init__(self, db: Session):
        self.db = db

    def create_pokemon(self, pokemon: PokemonCreate) -> Pokemon:
        db_pokemon = Pokemon(**pokemon.model_dump())
        self.db.add(db_pokemon)
        self.db.commit()
        self.db.refresh(db_pokemon)
        return db_pokemon

    def get_pokemons(self, skip: int = 0, limit: int = 10) -> list[Pokemon]:
        return self.db.query(Pokemon).offset(skip).limit(limit).all()

    def get_pokemon_by_name(self, name: str) -> Pokemon | None:
        all_pokemons = self.db.query(Pokemon).all()
        for pokemon in all_pokemons:
            if Levenshtein.distance(name.lower(), pokemon.name.lower()) <= 1:
                return pokemon
        return None
