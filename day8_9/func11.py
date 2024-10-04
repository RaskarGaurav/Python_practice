#!/usr/bin/python3

def maxi(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
n1=int(input())
n2=int(input())
n3=int(input())
print(maxi(n1,n2,n3))
