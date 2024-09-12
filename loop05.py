#!/usr/bin/python3

n = int(input("ENter a Number: "))
sum = 0
count =0
while(n>0):
	rem = n%10
	sum = sum + rem
	count = count+1
	n = n//10
print(count,sum)
