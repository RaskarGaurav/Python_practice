#!/usr/bin/python3

n = float(input("Enter Floating point number: "))

num, deno = (n).as_integer_ratio()

print(n," = ",num,"/",deno)
