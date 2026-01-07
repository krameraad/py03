import sys
import math


def dist(a: tuple, b: tuple) -> float:
    if len(a) != len(b):
        raise ValueError("points aren't of the same dimension")
    points = []
    for i in range(0, len(a)):
        points.append((a[i] - b[i]) ** 2)
    sum = 0
    for point in points:
        sum += point
    return math.sqrt(sum)


print("=== Game Coordinate System ===\n")
argc = len(sys.argv)
pos = tuple(sys.argv[0].split())
origin = (0, 0, 0)
print("Position created:", pos)
print(f"Distance between (0, 0, 0) and {pos}: {dist(origin, pos)}.")
tuple()
