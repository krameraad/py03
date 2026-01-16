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

print(f"{H}=== Command Quest ===\n{X}")
argc = len(sys.argv)
if (argc <= 1):
    print(f"{R}No arguments provided!{X}")
else:
    print(f"\033[1;4mArguments received: {argc - 1}{X}")
print("Program name:", sys.argv[0])
for i in range(1, argc):
    print(f"Argument {i}: {sys.argv[i]}")
print(f"{G}\nTotal arguments: {argc}{X}")
