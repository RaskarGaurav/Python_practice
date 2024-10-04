#!/usr/bin/python3

def rev(str):
    reve=""
    for i in str:
        reve=i+reve
    return reve

s="1234abcd"
print("String: ",s)
print("Reverse: ",rev(s))
