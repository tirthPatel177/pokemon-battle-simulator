from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base
from enum import Enum as PyEnum
import uuid

class BattleStatus(PyEnum):
    BATTLE_INPROGRESS = "BATTLE_INPROGRESS"
    BATTLE_COMPLETED = "BATTLE_COMPLETED"
    BATTLE_FAILED = "BATTLE_FAILED"

class Battle(Base):
    __tablename__ = "battles"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    pokemon_a_id = Column(Integer, ForeignKey('pokemons.id'), nullable=False)
    pokemon_b_id = Column(Integer, ForeignKey('pokemons.id'), nullable=False)
    current_round = Column(Integer, default=1, nullable=False)
    status = Column(Enum(BattleStatus), default=BattleStatus.BATTLE_INPROGRESS)
    winner_id = Column(Integer, ForeignKey('pokemons.id'), nullable=True)
    won_by_margin = Column(Integer, nullable=True)

    pokemon_a = relationship("Pokemon", foreign_keys=[pokemon_a_id])
    pokemon_b = relationship("Pokemon", foreign_keys=[pokemon_b_id])
    winner = relationship("Pokemon", foreign_keys=[winner_id])
