#!/usr/bin/python3

def keyDic(n):
    st=set()
    for i in n.keys():
        st.add(i)
    return st

dic={'Hello':12,'world':15,'Optimus':45}
print(keyDic(dic))
