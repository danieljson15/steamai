from steam_user import get_owned_games

# Replace this with your own SteamID64
steam_id = "demo"
games = get_owned_games(steam_id)

for g in games[:5]:  # print first 5 for sanity check
    print(f"{g['name']} ({g['appid']}): {g['playtime_minutes']} mins")