#!/usr/bin/python3

n = int(input("Enter a Number: "))
i=2
while(i<n):
	if(n%i==0):
		print("Not a pprime Number.")
		break
	i = i+1
else:
	print("Prime number.")
