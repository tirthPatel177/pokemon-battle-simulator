import pandas as pd
from sqlalchemy.orm import sessionmaker
from app.db.database import engine
from app.models.pokemon import Pokemon

df = pd.read_csv('./pokemon.csv')

Session = sessionmaker(bind=engine)
session = Session()

for index, row in df.iterrows():
    pokemon = Pokemon(
        name=row['name'],
        type1=row['type1'],
        type2=row['type2'] if pd.notna(row['type2']) else None,
        attack=int(row['attack']),
        against_bug=row['against_bug'],
        against_dark=row['against_dark'],
        against_dragon=row['against_dragon'],
        against_electric=row['against_electric'],
        against_fairy=row['against_fairy'],
        against_fight=row['against_fight'],
        against_fire=row['against_fire'],
        against_flying=row['against_flying'],
        against_ghost=row['against_ghost'],
        against_grass=row['against_grass'],
        against_ground=row['against_ground'],
        against_ice=row['against_ice'],
        against_normal=row['against_normal'],
        against_poison=row['against_poison'],
        against_psychic=row['against_psychic'],
        against_rock=row['against_rock'],
        against_steel=row['against_steel'],
        against_water=row['against_water']
    )
    session.add(pokemon)

try:
    session.commit()
    print("Pokemon data inserted successfully.")
except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()
