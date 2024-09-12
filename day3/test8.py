#!/usr/bin/python3

n= int(input("Enter Integer: "))
bina = bin(n)
length = len(bina)
print(bina[2:length])
