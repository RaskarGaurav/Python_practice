#!/usr/bin/python3

def ispal(str):
    return 1 if(str==str[::-1]) else 0

n=input()
print(ispal(n))
