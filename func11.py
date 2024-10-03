#!/usr/bin/python3

def isPerfect(n):
    tot=0
    for i in range(1,n):
        if(n%i==0):
            tot=tot+i
    return True if(tot==n) else False
num=int(input())
print(isPerfect(num))
