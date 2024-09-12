#!/usr/bin/python3
import math

n = int(input("Enter Integer: "))

sqroot  = math.sqrt(n)
if(sqroot%1==0): print("Perfect Square.")
else: print("Not a perfect Square.")
