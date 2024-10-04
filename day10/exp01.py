#!/usr/bin/python3

a=int(input())
b=int(input())
try:
    print(a/b)
except ZeroDivisionError:
    print("Dividing by Zero")
