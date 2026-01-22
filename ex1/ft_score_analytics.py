#!/usr/bin/env python3

import sys

X = "\033[0m"
R = "\033[91m"
D = "\033[2m"
H = "\033[1m"
HC = "\033[1;96m"

print(f"{H}\n=== Player Score Analytics ==={X}")
argc = len(sys.argv)
if argc <= 1:
    print(f"{R}No scores provided.{X}{D}\nUsage:"
          f" python3 ft_score_analytics.py <score1> <score2> ...{X}")
else:
    scores = []
    try:
        for i in range(1, argc):
            scores.append(int(sys.argv[i]))

        print(f"{HC}Scores processed{X}\t:", scores)
        totalscore = sum(scores)
        print(f"{HC}Total score{X}\t\t:", totalscore)
        highscore = max(scores)
        print(f"{HC}High score{X}\t\t:", highscore)
        lowscore = min(scores)
        print(f"{HC}Low score{X}\t\t:", lowscore)
        print(f"{HC}Score range{X}\t\t:", highscore - lowscore)

    except ValueError as e:
        print(f"{R}Error: {e.args[0]}{X}")
