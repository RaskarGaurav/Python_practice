#!/usr/bin/python3

n= int(input("Enter odd numbers only: "))

sp = n//2
st = 1
for i in range(1,n//2+2):
	print(" "*sp,"*"*st,sep="")
	st = st+2
	sp = sp-1

st =n-2
sp = 1
for i in range(1,n//2+1):
	print(" "*sp,"*"*st,sep="")
	st = st-2
	sp = sp+1
