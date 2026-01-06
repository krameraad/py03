import sys

print("=== Player Score Analytics ===")
argc = len(sys.argv)
if argc <= 1:
    print("No scores provided. Usage:"
          " python3 ft_score_analytics.py <score1> <score2> ...")
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
