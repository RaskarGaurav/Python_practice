#!/usr/bin/python3
sum = 0
for i in range(1,21):
	n = int(input("Enter "+str(i)+"th number: "))
	sum = sum+n if (n%2==0) else sum
print("Sum: ",sum)
