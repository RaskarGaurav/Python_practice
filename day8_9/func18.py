#!/usr/bin/python3

def distin(l):
    st=set(l)
    return list(st)

lst=[1,2,3,3,3,3,4,5]
print("Original: ",lst)
print("Unique: ",distin(lst))
