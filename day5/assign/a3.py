#!/usr/bin/python3
str1 = input("Enter a String: ")
str2 = input("Enter a String: ")
n = len(str1)//2
m = len(str2)//2
print(str1[0]+str1[n]+str1[-1]+str2[0]+str2[m]+str2[-1])
