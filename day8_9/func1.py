#!/usr/bin/python3

def countStr(str):
    cntu=0
    cntl=0
    for i in str:
        if i.isupper():
            cntu=cntu+1
        elif i.islower():
            cntl=cntl+1
    return cntu,cntl
n=input()
tup=countStr(n)
print('Upper: ',tup[0])
print('lower: ',tup[1])
