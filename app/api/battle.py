from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.models.battle import BattleStatus
from app.schemas.battle import BattleCreate, BattleRead, BattleResult
from app.services.battle_service import BattleService
from app.services.pokemon_service import PokemonService
from app.db.database import get_db

router = APIRouter()

@router.post("/battles/", response_model=BattleRead)
def create_battle(battle_data: BattleCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    battle_service = BattleService(db)
    pokemon_service = PokemonService(db)

    pokemon_a = pokemon_service.get_pokemon_by_name(battle_data.pokemon_a_name)
    pokemon_b = pokemon_service.get_pokemon_by_name(battle_data.pokemon_b_name)

    if not pokemon_a or not pokemon_b:
        raise HTTPException(status_code=404, detail="One or both Pokémon not found")

    battle = battle_service.create_battle(pokemon_a, pokemon_b)
    
    # Run the battle in the background
    background_tasks.add_task(battle_service.run_battle, battle.id)

    return BattleRead(
        id=battle.id,
        pokemon_a_name=pokemon_a.name,
        pokemon_b_name=pokemon_b.name,
        current_round=battle.current_round,
        status=battle.status,
        result=None  # Initial response, battle not completed yet
    )

@router.get("/battles/{battle_id}", response_model=BattleRead)
def get_battle(battle_id: int, db: Session = Depends(get_db)):
    battle_service = BattleService(db)
    battle = battle_service.get_battle(battle_id)
    if not battle:
        raise HTTPException(status_code=404, detail="Battle not found")

    result = None
    if battle.status == BattleStatus.COMPLETED:
        result = BattleResult(
            winnerName=battle.winner.name if battle.winner else None,
            wonByMargin=battle.won_by_margin
        )

    return BattleRead(
        id=battle.id,
        pokemon_a_name=battle.pokemon_a.name,
        pokemon_b_name=battle.pokemon_b.name,
        current_round=battle.current_round,
        status=battle.status,
        result=result
    )
