#!/usr/bin/python3

try:
    n=int(input())
except ValueError:
    print("Raising TypeError.")
    raise TypeError
