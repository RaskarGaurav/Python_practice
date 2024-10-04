#!/usr/bin/python3

l1=[10,20,30,40]
l2=[100,200,300,400]

for i in range(max(len(l1),len(l2))):
    if(i<min(len(l1),len(l2))):
        print(l1[i]," ",l2[len(l2)-i-1])
    else:
        if(len(l1)<len(l2)):
            print("   ",l2[len(l2)-i-1])
        else:
            print(l1[i])
