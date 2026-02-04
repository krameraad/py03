#!/usr/bin/env python3

X = "\033[0m"
H = "\033[1m"
HC = "\033[1;96m"

data: dict[str, dict | list[str]] = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "achievements_count": 5
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "achievements_count": 2
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "achievements_count": 7
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "achievements_count": 4
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "achievements_count": 7
        },
        "frank": {
            "level": 15,
            "total_score": 359,
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

high_scorers = [k for k, v in data["players"].items()
                if v["total_score"] > 2000]
print(f"{HC}High scorers (>2000){X}\t: {high_scorers}")

scores_doubled = [v["total_score"] * 2
                  for v in data["players"].values()]
print(f"{HC}Scores doubled{X}\t\t: {scores_doubled}")

active_players = [k for k in data["players"]]
print(f"{HC}Active players{X}\t\t: {active_players}")


print(f"{H}\n=== Dict Comprehension Examples ==={X}")

player_scores = {k: v["total_score"]
                 for k, v in data["players"].items()}
print(f"{HC}Player scores{X}\t\t: {player_scores}")

score_categories = {
    "high": len([k for k, v in data["players"].items()
                 if v["total_score"] > 2000]),
    "medium": len([k for k, v in data["players"].items()
                   if v["total_score"] > 1000]),
    "low": len([k for k, v in data["players"].items()
                if v["total_score"] <= 1000])
}
print(f"{HC}Score categories{X}\t: {score_categories}")

achievement_counts = {k: v["achievements_count"]
                      for k, v in data["players"].items()}
print(f"{HC}Achievement counts{X}\t: {achievement_counts}")


print(f"{H}\n=== Set Comprehension Examples ==={X}")

unique_players = {k for k in data["players"]}
print(f"{HC}Unique players{X}\t\t: {unique_players}")

unique_achievements = {k for k in data["achievements"]}
print(f"{HC}Unique achievements{X}\t: {unique_achievements}")

active_regions = {k for k in data["regions"]
                  if "w" not in k}
print(f"{HC}Active regions{X}\t\t: {active_regions}")


print(f"{H}\n=== Combined Analysis ==={X}")
print(f"{HC}Total players{X}\t\t\t: {len(active_players)}")
print(f"{HC}Total unique achievements{X}\t: {len(unique_achievements)}")
print(f"{HC}Average score{X}\t\t\t: "
      f"{sum(scores_doubled) / len(scores_doubled) / 2:.1f}")

top_performer = ("", -1)
for k, v in data["players"].items():
    if v["total_score"] > top_performer[1]:
        top_performer = (k, v["total_score"])
print(f"{HC}Top performer{X}\t\t\t: {top_performer[0]}")
