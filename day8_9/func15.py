#!/usr/bin/python3

def factorial(n):
    if(n>1):
        return n*factorial(n-1)
    else:
        return 1

num=int(input())
print(factorial(num))
