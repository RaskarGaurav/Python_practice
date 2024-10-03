#!/usr/bin/python3

str1 = ""
str2 = ""
if(len(str1)>1):
    str1 = str1[1]+str1[0]+str1[2:]
if(len(str2)>1):
    str2 = str2[1]+str2[0]+str2[2:]

print(str1+" "+str2)
