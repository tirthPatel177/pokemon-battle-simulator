from pydantic import BaseModel
from enum import Enum

class BattleStatus(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class BattleBase(BaseModel):
    pokemon_a_name: str
    pokemon_b_name: str

class BattleCreate(BattleBase):
    pass

class BattleResult(BaseModel):
    winnerName: str | None
    wonByMargin: int | None

class BattleRead(BaseModel):
    id: int
    current_round: int
    status: BattleStatus
    result: BattleResult | None

    class Config:
        orm_mode = True
