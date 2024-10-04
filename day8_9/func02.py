#!/usr/bin/python3

def isdiv11(l):
    l1=[]
    for i in l:
        if(i%11==0): l1.append(i)
    return l1

lst= [11,10,12,22,110,121,85,45]
print(isdiv11(lst))
