#!/usr/bin/python3
str = input("Enter a String: ")
str1 = ""
for i in str:
    if(i<"a"):
        str1 = str1 + i
    else:
        str1 = i + str1

print(str1)
