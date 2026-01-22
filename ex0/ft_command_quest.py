#!/usr/bin/env python3

import sys

X = "\033[0m"
R = "\033[91m"
Y = "\033[93m"
H = "\033[1m"
HC = "\033[1;96m"

print(f"{H}\n=== Command Quest ==={X}")
argc = len(sys.argv)
if (argc <= 1):
    print(f"{R}No arguments provided!{X}")
else:
    print(f"{H}Arguments received: {Y}{argc - 1}{X}")
print(f"- {HC}Program name{X}\t:", sys.argv[0])
for i in range(1, argc):
    print(f"- {HC}Argument {i}{X}\t: {sys.argv[i]}")
print(f"\n{H}Total arguments: {Y}{argc}{X}")
