# Pokémon Battle Simulator

## Overview

The Pokémon Battle Simulator is a FastAPI application that simulates battles between Pokémon. Users can create Pokémon, initiate battles, and fetch battle results. Battles are processed asynchronously.

## Features

- Create and list Pokémon with attributes.
- Start a battle between two Pokémon.
- Check the status and results of a battle.
- Health check endpoint for monitoring.

## Setup

### Prerequisites

- Python 3.9+ / 3.11 preffered
- PostgreSQL
- `pip` (Python package installer)

### Environment Variables

Create a `.env` file in the root directory with the following:

```plaintext
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=newPassword
DB_NAME=pokemon_battle_simulator
```


### Installation
1. Install dependencies:

```
pip install -r requirements.txt
```

2. Set up the database:
```
psql -U postgres -d postgres -c "CREATE DATABASE pokemon_battle_simulator;"
```

3. Insert initial data:
```
python insertDataToDBFromCSV.py
```

### Running the Application
Start the server:

```
fastapi dev app/main.py
```

Access the application at http://localhost:8000.


### Testing
```
pytest --cov=app tests/
```

### Note
I have deployed this on a free hosting service which may get down due to inactivity. Please retry after 1-2 min if something isn't working.