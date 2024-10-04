#!/usr/bin/python3

def eve(l):
    l1=[]
    for i in l:
        if(i%2==0): l1.append(i)
    return l1

lst=[1,2,3,4,5,6,7,8,9]
print(lst)
print(eve(lst))
