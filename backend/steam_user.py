'''import os
import requests
from dotenv import load_dotenv

load_dotenv()
STEAM_API_KEY = os.getenv("STEAM_API_KEY")

def get_owned_games(steam_id):
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        "key": STEAM_API_KEY,
        "steamid": steam_id,
        "include_appinfo": 0,  # include game names, images, etc.
        "include_played_free_games": 1
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Steam API call failed:", response.text)
        raise Exception(f"Steam API error: {response.status_code}")

    games = response.json().get("response", {}).get("games", [])
    formatted = [
        {
            "appid": game["appid"],
            "name": game["name"],
            "playtime_minutes": game.get("playtime_forever", 0)
        }
        for game in games
    ]

    return formatted 
    '''
import json

def get_owned_games(steam_id):
    if steam_id == "demo":
        with open("demo_user_data.json") as f:
            return json.load(f)

    if not STEAM_API_KEY:
        raise Exception("Missing Steam API key! Did you load your .env?")

    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        "key": STEAM_API_KEY,
        "steamid": steam_id,
        "include_appinfo": 0,  # safe mode
        "include_played_free_games": 1
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Steam API response text:", response.text)
        raise Exception(f"Steam API error: {response.status_code}")

    games = response.json().get("response", {}).get("games", [])
    formatted = [
        {
            "appid": game["appid"],
            "name": game.get("name", f"AppID {game['appid']}"),
            "playtime_minutes": game.get("playtime_forever", 0)
        }
        for game in games
    ]
    return formatted