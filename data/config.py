import json
import os


# Location of the config file
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")

def load_default_city() -> str | None:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            data = json.load(file)
            return data.get('default_city')
        
    return None

def save_default_city(city: str) -> None:
    with open(CONFIG_FILE, 'w') as file:
        json.dump({"default_city": city}, file)
