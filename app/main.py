from fastapi import FastAPI
from app.db.database import engine, Base  

from app.models import pokemon, battle, round

from app.api.pokemon import router as pokemon_router
from app.api.battle import router as battle_router
from app.api.health import router as health_router

def create_app():
    app = FastAPI()

    Base.metadata.create_all(bind=engine)  

    app.include_router(pokemon_router, prefix="/api/v1/pokemon", tags=["Pokemon"])
    app.include_router(battle_router, prefix="/api/v1/battle", tags=["Battle"])
    app.include_router(health_router, tags=["Health"])

    return app

app = create_app()
