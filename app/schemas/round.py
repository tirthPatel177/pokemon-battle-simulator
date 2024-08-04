from pydantic import BaseModel

class RoundBase(BaseModel):
    battle_id: int
    attacker_id: int
    defender_id: int
    attack_used: str
    damage_dealt: int
    round_result: str

class RoundCreate(RoundBase):
    pass

class RoundRead(RoundBase):
    id: int

    class Config:
        orm_mode = True