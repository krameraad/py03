#!/usr/bin/env python3

import sys
import math

X = "\033[0m"
R = "\033[91m"
D = "\033[2m"
H = "\033[1m"
HC = "\033[1;96m"


def dist3(a: tuple, b: tuple) -> float:
    """Find the distance between two three-dimensional points."""
    len_a, len_b = len(a), len(b)
    if len_a != len_b or len_a != 3:
        raise ValueError("invalid point dimensions")
    sum = 0
    for i in range(0, 3):
        sum += (int(a[i]) - int(b[i])) ** 2
    return math.sqrt(sum)


print(f"{H}\n=== Game Coordinate System ==={X}")
try:
    pos = tuple(sys.argv[1].split(','))
    origin = (0, 0, 0)
    print(f"{HC}Position created{X}:", pos)
    print(f"{HC}Distance between (0, 0, 0) and {pos}{X}: {dist3(origin, pos)}")
    print(f"{D}\nUnpacking demonstration:{X}")
    a, b, c = pos
    print(f"{HC}Player at{X}: x={a}, y={b}, z={c}")
except ValueError as e:
    print(f"{R}Error parsing coordinates: {str(e)}{X}")
    print(f"{D}\n- Usage: ft_coordinate_system.py x,y,z{X}")
except IndexError:
    print(f"{R}Error: no arguments provided{X}")
    print(f"{D}\n- Usage: ft_coordinate_system.py x,y,z{X}")
