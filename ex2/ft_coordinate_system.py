#!/usr/bin/env python3

import sys
import math

X = "\033[0m"
R = "\033[91m"
D = "\033[2m"
H = "\033[1m"
HC = "\033[1;96m"

Vec3D = tuple[float, float, float]


def dist3(a: Vec3D, b: Vec3D) -> float:
    """Find the distance between two three-dimensional points."""
    sum = 0
    for i in range(0, 3):
        sum += (a[i] - b[i]) ** 2
    return math.sqrt(sum)


print(f"{H}\n=== Game Coordinate System ==={X}")
try:
    pos = tuple(sys.argv[1].split(','))

    if len(pos) != 3:
        raise ValueError("invalid point dimensions")

    origin = (0, 0, 0)
    print(f"{HC}Position created{X}: {pos}\n"
          f"{HC}Distance between (0, 0, 0) and {pos}{X}:"
          f" {dist3(origin, tuple([float(x) for x in pos])):.3f}")

    print(f"{D}\nUnpacking demonstration:{X}")
    a, b, c = pos
    print(f"{HC}Player at{X}: x={a}, y={b}, z={c}")
    # print(f"{HC}Player at{X}: "
    #       "x={}, y={}, z={}".format(*pos))

except ValueError as e:
    print(f"{R}Error parsing coordinates: {e}{X}")
    print(f"{D}\n- Usage: ft_coordinate_system.py x,y,z{X}")

except IndexError:
    print(f"{R}Error: no arguments provided{X}")
    print(f"{D}\n- Usage: ft_coordinate_system.py x,y,z{X}")
