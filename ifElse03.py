#!/usr/bin/python3

tot_class = int(input("Enter total Lectures: "))
att_class = int(input("Enter attended Lectures: "))

percent = att_class*100/tot_class
print(percent)
if(percent<75) :
	ch = input("Do you have any medical Cause?(y/n)")
	if(ch=="y") :
		print("allowed for exam.")
	else :
		print("Not allowed for exam.")
else :
	print("allowed for exam.")
