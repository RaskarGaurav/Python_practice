#!/usr/bin/python3

def rollcheck(n):
    st=set()
    for i,j in n.items():
        if(j==100): st.add(i)
    return st
dic={'walter':101,'Jesse':100,'Hank':103,'Skyler':104}
print(rollcheck(dic))
