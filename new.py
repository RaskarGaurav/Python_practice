#!/usr/bin/python3
n = int(input())
l = []
k = 1
for i in range(n):
    l.append(int(input()))
print(l)
while(k<=n):
    for i in range(n) :
        if(l[i]==k):
            print(i+1,end=" ")
            break
    k= k+1
