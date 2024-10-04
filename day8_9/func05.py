#!/usr/bin/python3

def alterstr(str):
    str1=""
    for i in range(1,len(str),2):
        str1=str1+str[i]
    return str1

n=input()
print(alterstr(n))
