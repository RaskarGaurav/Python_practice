#!/usr/bin/python3
n = int(input("Enter odd Number: "))

st = n-1
sp = 0
for i in range(n):
	print(" "*sp,"10"*st,"1",sep="")
	st = st - 1
	sp = sp+1
