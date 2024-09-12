#!/usr/bin/python3

n = int(input("Enter prize of bike: "))
tax =0
insu =0
if(n<=50000):
	tax =insu= n*0.05
	n = n*1.1
elif(50000<n<=100000):
	tax = n*0.10
	insu = n*0.08
	n = n*1.18
elif(n>100000):
	tax = insu = n*0.15
	n = n*1.3

print("Tax: ",tax)
print("Insurance: ",insu)
print("Total Prize: ",n)
