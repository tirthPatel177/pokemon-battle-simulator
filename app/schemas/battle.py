from pydantic import BaseModel
from enum import Enum

class BattleStatus(str, Enum):
    BATTLE_INPROGRESS = "BATTLE_INPROGRESS"
    BATTLE_COMPLETED = "BATTLE_COMPLETED"
    BATTLE_FAILED = "BATTLE_FAILED"

class BattleBase(BaseModel):
    pokemon_a_name: str
    pokemon_b_name: str

class BattleCreate(BattleBase):
    pass

class BattleResult(BaseModel):
    winnerName: str | None
    wonByMargin: int | None

class BattleRead(BaseModel):
    id: str
    status: BattleStatus
    result: BattleResult | None

    class Config:
        orm_mode = True
