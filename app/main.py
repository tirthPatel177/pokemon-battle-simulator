from fastapi import FastAPI
from app.db.database import engine, Base  # Import Base here directly from db.database

# Import models after Base has been imported
from app.models import pokemon, battle, round

# Import API routers
from app.api.pokemon import router as pokemon_router
from app.api.battle import router as battle_router

def create_app():
    app = FastAPI()

    # Create database tables
    Base.metadata.create_all(bind=engine)  # This creates all tables based on the models defined

    # Include routers
    app.include_router(pokemon_router, prefix="/api/v1/pokemon", tags=["Pokemon"])
    app.include_router(battle_router, prefix="/api/v1/battle", tags=["Battle"])

    return app

app = create_app()
