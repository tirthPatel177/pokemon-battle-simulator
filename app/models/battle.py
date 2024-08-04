# app/models/battle.py

from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base
from enum import Enum as PyEnum

class BattleStatus(PyEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Battle(Base):
    __tablename__ = "battles"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_a_id = Column(Integer, ForeignKey('pokemons.id'), nullable=False)
    pokemon_b_id = Column(Integer, ForeignKey('pokemons.id'), nullable=False)
    current_round = Column(Integer, default=1, nullable=False)
    status = Column(Enum(BattleStatus), default=BattleStatus.IN_PROGRESS)
    winner_id = Column(Integer, ForeignKey('pokemons.id'), nullable=True)

    pokemon_a = relationship("Pokemon", foreign_keys=[pokemon_a_id])
    pokemon_b = relationship("Pokemon", foreign_keys=[pokemon_b_id])
    winner = relationship("Pokemon", foreign_keys=[winner_id])
