#!/usr/bin/python3

def checkStr(l):
    l1=[]
    for i in l:
        if(i.count('s')==2): l1.append(i)
    return l1
lst=['vsfvsv','Hello','gsiovsn','World']
print(checkStr(lst))
