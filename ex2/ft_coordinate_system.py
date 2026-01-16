#!/usr/bin/env python3

import sys
import math

X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
D = "\033[2m"
H = "\033[1m"
E = "\033[3m"


def dist3(a: tuple, b: tuple) -> float:
    """Find the distance between two three-dimensional points."""
    len_a, len_b = len(a), len(b)
    if len_a != len_b or len_a != 3:
        raise ValueError("invalid point dimensions")
    sum = 0
    for i in range(0, 3):
        sum += (int(a[i]) - int(b[i])) ** 2
    return math.sqrt(sum)


print(f"{H}=== Game Coordinate System ==={X}\n")
try:
    pos = tuple(sys.argv[1].split(','))
    origin = (0, 0, 0)
    print("Position created:", pos)
    print(f"{G}Distance between (0, 0, 0) and {pos}: {dist3(origin, pos)}{X}")
    print(f"{D}\nUnpacking demonstration:{X}")
    a, b, c = pos
    print(f"Player at: x={a}, y={b}, z={c}")
except ValueError as e:
    print(f"{R}Error parsing coordinates: {str(e)}{X}")
    print(f"{E}\n- Usage: ft_coordinate_system.py x,y,z{X}")
except IndexError:
    print(f"{R}Error: no arguments provided{X}")
    print(f"{E}\n- Usage: ft_coordinate_system.py x,y,z{X}")
