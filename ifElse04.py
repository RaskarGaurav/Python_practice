#!/usr/bin/python3

tot_marks = int(input("Enter total marks: "))
obt_marks = int(input("Enter obtained marks: "))
percent = obt_marks*100/tot_marks
print(percent)

if(percent<25):
	print("grade: F")
elif(25<percent<=45):
	print("grade: E")
elif(45<percent<=50):
	print("grade: D")
elif(50<percent<=60):
	print("grade: C")
elif(60<percent<=80):
	print("grade: B")
elif(80<percent):
	print("grade: A")





