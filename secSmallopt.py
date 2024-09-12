#!/usr/bin/python3

l1 = [67,3,45,89,900,23,12,234,145]

mn = min(l1)
l2 = [i for i in l1 if(i!=mn)]
print(min(l2))

for i in range(len(l1)-1):
    if(l1[i+1]<l1[i]):
        mn = l1[i+1]
for i in range(len(l1)-1):
    if(l1[i+1]<l1[i]<mn):
        mn1 = l1[i+1]

print(mn1)
