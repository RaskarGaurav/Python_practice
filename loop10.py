#!/usr/bin/python3
n = int(input("Enter Number: "))
x = int(input("Enter x: "))
for i in range(n):
	t = (-1)**i*(x**(2*i+1))
	print(t)
