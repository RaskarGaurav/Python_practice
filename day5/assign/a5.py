#!/usr/bin/python3
import math
str1 = input("Enter string: ")
str2 = input("Enter string: ")
i = 0
str3 =""
mx = max(len(str1),len(str2))
while i<mx :
    if(i<len(str1)):
        str3 = str3 + str1[i]
    if(i<len(str2)):
        str3 = str3 + str2[i]
    i = i+1
print(str3)
