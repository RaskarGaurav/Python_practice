#!/usr/bin/python3

lst=[1,2,3]
try:
    n=lst[3]
except IndexError:
    print("Stay in limits...")
