#!/usr/bin/python3

sum = 0
product = 1
while(True):
	n = int(input("Enter a Number: "))
	sum = sum + n
	product = product*n
	q = input("Press 'q' to Quit: ")
	if(q=="q"):
		break
print(sum,product)
