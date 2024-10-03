#!/usr/bin/python3

def checkDic(l):
    str='id'
    l1=[]
    for i in l:
        if(str in i):
            l1.append(i)
    return l1
lst=[{'ab':1,'bc':2},{'id':3,'kd':4},{'uj':5,'id':6}]
print(checkDic(lst))
