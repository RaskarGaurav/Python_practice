#!/usr/bin/python3

unit = int(input("Enter unit: "))
total_bill = 0

if(unit>200) :
	total_bill = 500 + (unit-200)*10
elif(unit>100) :
	total_bill = 5*(unit-100)
else :
	print("No Bill Hurray!")

print("Total Bill: ",total_bill)
