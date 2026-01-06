#!/usr/bin/python3

import sys

print("=== Command Quest ===")
argc = len(sys.argv)
if (argc <= 1):
    print("No arguments provided!")
print("Program name:", sys.argv[0])
if (argc > 1):
    print("Arguments received:", argc - 1)
for i in range(1, argc):
    print(f"Argument {i}: {sys.argv[i]}")
print("Total arguments:", argc)
