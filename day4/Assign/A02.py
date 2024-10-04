#!/usr/bin/python3

l1=[x for x in range(150,251) if(x%2==0)]
print(len(l1))

l2=[i for i in l1 if(i%4==2)]
print(l2)
