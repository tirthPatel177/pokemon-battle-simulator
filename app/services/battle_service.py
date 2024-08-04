# services/battle_service.py

from sqlalchemy.orm import Session
from app.models.battle import Battle, BattleStatus
from app.models.round import Round
from app.models.pokemon import Pokemon
from time import sleep

class BattleService:
    def __init__(self, db: Session):
        self.db = db

    def create_battle(self, pokemon_a: Pokemon, pokemon_b: Pokemon) -> Battle:
        battle = Battle(
            pokemon_a_id=pokemon_a.id,
            pokemon_b_id=pokemon_b.id,
            status=BattleStatus.IN_PROGRESS
        )
        self.db.add(battle)
        self.db.commit()
        self.db.refresh(battle)
        return battle

    def run_battle(self, battle_id: int):
        battle = self.db.query(Battle).filter(Battle.id == battle_id).first()
        if not battle:
            return

        try:
            # Simulate round processing
            for round_number in range(1, 3):  # Assuming 2 rounds
                if round_number == 1:
                    attacker = battle.pokemon_a
                    defender = battle.pokemon_b
                else:
                    attacker = battle.pokemon_b
                    defender = battle.pokemon_a

                damage = self.calculate_damage(attacker, defender)
                round_result = Round(
                    battle_id=battle.id,
                    attacker_id=attacker.id,
                    defender_id=defender.id,
                    attack_used="default_attack",  # Example attack name
                    damage_dealt=damage,
                    round_result=f"{attacker.name} attacked {defender.name} dealing {damage} damage"
                )
                self.db.add(round_result)
                self.db.commit()

                sleep(5)  # Simulate delay

            self.determine_winner(battle.id)
        except Exception as e:
            battle.status = BattleStatus.FAILED
            self.db.commit()

    def calculate_damage(self, attacker: Pokemon, defender: Pokemon) -> int:
        attack_value = attacker.attack
        against_type1 = getattr(defender, f"against_{attacker.type1}", 1)
        against_type2 = getattr(defender, f"against_{attacker.type2}", 1) if attacker.type2 else 1

        damage = (attack_value / 200) * 100 - ((against_type1 / 4) * 100 + (against_type2 / 4) * 100)
        return int(damage)

    def determine_winner(self, battle_id: int):
        battle = self.db.query(Battle).filter(Battle.id == battle_id).first()
        if not battle:
            return

        # Assuming two rounds
        round_1 = self.db.query(Round).filter(Round.battle_id == battle.id, Round.attacker_id == battle.pokemon_a_id).first()
        round_2 = self.db.query(Round).filter(Round.battle_id == battle.id, Round.attacker_id == battle.pokemon_b_id).first()

        if round_1.damage_dealt > round_2.damage_dealt:
            battle.winner_id = battle.pokemon_a_id
            battle.won_by_margin = round_1.damage_dealt
        elif round_2.damage_dealt > round_1.damage_dealt:
            battle.winner_id = battle.pokemon_b_id
            battle.won_by_margin = round_2.damage_dealt
        else:
            battle.winner_id = None  # Draw
            battle.won_by_margin = 0

        battle.status = BattleStatus.COMPLETED
        self.db.commit()

    def get_battle(self, battle_id: int) -> Battle:
        return self.db.query(Battle).filter(Battle.id == battle_id).first()
