#!/usr/bin/python3

d1={1:500,4:300,3:400}
d2={}
for i,v in sorted(d1.items(),key=lambda k:(k[1])):
    d2[i]=v

print(d2)
