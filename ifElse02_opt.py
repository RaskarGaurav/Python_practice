#!/usr/bin/python3

amt = int(input("Enter amount: "))

if(amt>=2000) :
	print("2000-> ",(amt//2000))
	amt = amt-(amt//2000)*2000
if(amt>=500) :
	print("500->",(amt//500))
	amt = amt-(amt//500)*500
if(amt>=100) :
	print("100->.",amt//100)
	amt = amt-(amt//100)*100
if(amt>=50) :
	print("50-> ",amt//50)
	amt = amt - (amt//50)*50
if(amt>=10) :
	print("10-> ",amt//10)
	amt = amt - (amt//10)*10
if(amt>=5) :
	print("5-> ",amt//5)
	amt = amt - (amt//5)*5
if(amt>=2) :
	print("2-> ",amt//2)
	amt = amt - (amt//2)*2
if(amt>=1) :
	print("1-> ",amt//1)
	amt = amt - (amt//1)*1
