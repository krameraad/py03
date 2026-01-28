#!/usr/bin/env python3

X = "\033[0m"
D = "\033[2m"
H = "\033[1m"
HC = "\033[1;96m"
HY = "\033[1;93m"
XH = "\033[0;1m"

data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1
        }
    },
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer"
    ],
    "regions": [
        "north",
        "east",
        "central",
        "west",
        "north"
    ]
}


print(f"{H}\n=== Game Analytics Dashboard ==={X}")


print(f"{H}\n=== List Comprehension Examples ==={X}")

high_scorers = [player for player in data["players"]
                if data["players"][player]["total_score"] > 2000]
print(f"{HC}High scorers (>2000){X}\t: {high_scorers}")

scores_doubled = [player["total_score"] * 2
                  for player in data["players"].values()]
print(f"{HC}Scores doubled{X}\t\t: {scores_doubled}")

active_players = [player for player in data["players"]]
print(f"{HC}Active players{X}\t\t: {active_players}")


print(f"{H}\n=== Dict Comprehension Examples ==={X}")

player_scores = {player: data["players"][player]["total_score"]
                 for player in data["players"]}
print(f"{HC}Player scores{X}\t\t: {player_scores}")

score_categories = {category: data["players"][category]["total_score"]
                    for category in data["players"]}
print(f"{HC}Score categories{X}\t: {score_categories}")

achievement_counts = {player: data["players"][player]["achievements_count"]
                      for player in data["players"]}
print(f"{HC}Achievement counts{X}\t: {achievement_counts}")


print(f"{H}\n=== Set Comprehension Examples ==={X}")

unique_players = {player for player in data["players"]}
print(f"{HC}Unique players{X}\t\t: {unique_players}")

unique_achievements = {achievement for achievement in data["achievements"]}
print(f"{HC}Unique achievements{X}\t: {unique_achievements}")

active_regions = {region for region in data["regions"]
                  if "w" not in region}
print(f"{HC}Active regions{X}\t\t: {active_regions}")


print(f"{H}\n=== Combined Analysis ==={X}")
print(f"{HC}Total players{X}\t\t\t: {len(active_players)}")
print(f"{HC}Total unique achievements{X}\t: {1}")
print(f"{HC}Average score{X}\t\t\t: "
      f"{sum(scores_doubled) / len(scores_doubled) / 2:.1f}")
print(f"{HC}Top performer{X}\t\t\t: {1}")
