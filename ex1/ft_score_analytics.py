#!/usr/bin/env python3

import sys

X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
D = "\033[2m"
H = "\033[1m"

print("=== Player Score Analytics ===")
argc = len(sys.argv)
if argc <= 1:
    print(f"{R}No scores provided.{X}{D}\nUsage:"
          f" python3 ft_score_analytics.py <score1> <score2> ...{X}")
else:
    scores = []
    for i in range(1, argc):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError as e:
            print("Error:", e.args[0])
    print("Scores processed:", scores)
    totalscore = sum(scores)
    print("Total score:", totalscore)
    highscore = max(scores)
    print("High score:", highscore)
    lowscore = min(scores)
    print("Low score:", lowscore)
    print("Score range:", highscore - lowscore)
