#!/usr/bin/python3

n = int(input("Enter a number: "))
total = 0
for i in range(n+1):
	total = total + i if (i%2!=0) else total

print("Total of odd numbers till",n," : ",total)
