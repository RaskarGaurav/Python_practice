#!/usr/bin/python3

l1 = [5,7,9,12]
l2 = [7,9]
l3 = [12,7]
for j in l3:
    if j not in l1:
        print("Not sublist")
        break
else :
    print("Sublist")

