#!/usr/bin/python3

n = int(input("Enter year: "))
if((n%100!=0 and n%4==0)or n%400==0):
	print(n," is a Leap year.")
else:
	print(n," is Not a leap year")
