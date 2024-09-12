#!/usr/bin/python3

tot_class = int(input("Enter total lectures: "))
att_class = int(input("Enter attended lectures: "))

percent = att_class*100/tot_class

print(percent)

if(percent>=75) :
	print("Allowed for Exam.")
else :
	print("NO allowed for Exam.")
