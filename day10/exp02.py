#!/usr/bin/python3

try:
    n=int(input())
    print("Coorect Input: ",n)
except ValueError:
    print("Not correct type of input.")
    raise
