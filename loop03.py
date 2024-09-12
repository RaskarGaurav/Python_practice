#!/usr/bin/python3
a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
min= a if(a<b) else b
gcd =1
for i in range(1,min+1):
	if(a%i==0 and b%i==0):
		gcd=i
print("GCD: ",gcd)
