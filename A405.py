#!/usr/bin/python3

for i in range(0,101):
    print(i,end=" ")
    if(i%3==0):
        print(i)
    elif(i%5==0):
        print(i)
    elif(i%3==0 and i%5==0):
        print(i)
