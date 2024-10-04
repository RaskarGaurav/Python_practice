#!/usr/bin/python3

def mulList(l):
    mul=1
    for i in l:
        mul*=i
    return mul
lst=[8,2,3,-1,7]
print(lst)
print(mulList(lst))
