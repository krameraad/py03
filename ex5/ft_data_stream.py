#!/usr/bin/env python3

X = "\033[0m"
R = "\033[91m"
G = "\033[92m"
B = "\033[94m"
C = "\033[96m"
M = "\033[95m"
Y = "\033[93m"
HY = "\033[1;93m"
D = "\033[2m"
H = "\033[1m"
HC = "\033[1;96m"
XH = "\033[0;1m"
E = "\033[3m"


def stream_processor(count: int):
    print(f"{D}Processing {count} game events...")


def fibonacci(limit: int):
    a, b = 0, 1
    yield a
    while True:
        a, b = b, a + b
        yield b


def primes(limit: int):
    pass


print(f"{H}=== Game Data Stream Processor ==={X}")
print(f"{H}=== Stream Analytics ==={X}")
print(f"{H}=== Generator Demonstration ==={X}")
limit = 10
print(f"Fibonacci sequence (first {limit}): {fibonacci(limit)}")
