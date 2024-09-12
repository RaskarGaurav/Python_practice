#!/usr/bin/python3

amt = int(input("Enter Amount: "))
n2000=0
n500=0
n100=0
n50=0
n10=0
n5=0
n2=0
n1=0
while amt>0 :
	if(amt>=2000) :
		amt-=2000
		n2000+=1
	elif(amt>=500) :
		amt-=500
		n500+=1
	elif(amt>=100) :
		amt-=100
		n100+=1
	elif(amt>=50) :
		amt-=50
		n50+=1
	elif(amt>=10) :
		amt-=10
		n10+=1
	elif(amt>=5) :
		amt-=5
		n5+=5
	elif(amt>=2) :
		amt-=2
		n2+=2
	elif(amt>=1) :
		amt-=1
		n1+=1

print(amt)
print("2000-> ",n2000)
print("500-> ",n500)
print("100-> ",n100)
print("50-> ",n50)
print("10-> ",n10)
print("5-> ",n5)
print("2-> ",n2)
print("1-> ",n1)

