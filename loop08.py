#!/usr/bin/python3

n = int(input("Enter number: "))
total = 0

for i in range(1,n+1):
	t= "9"*i
	total= total + int(t)
print("Sum: ",total)
