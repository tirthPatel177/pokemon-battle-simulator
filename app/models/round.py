# app/models/round.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Round(Base):
    __tablename__ = "rounds"

    id = Column(Integer, primary_key=True, index=True)
    battle_id = Column(Integer, ForeignKey('battles.id'), nullable=False)
    attacker_id = Column(Integer, ForeignKey('pokemons.id'), nullable=False)
    defender_id = Column(Integer, ForeignKey('pokemons.id'), nullable=False)
    attack_used = Column(String, nullable=False)
    damage_dealt = Column(Integer, nullable=False)
    round_result = Column(String, nullable=False)

    battle = relationship("Battle")
    attacker = relationship("Pokemon", foreign_keys=[attacker_id])
    defender = relationship("Pokemon", foreign_keys=[defender_id])
