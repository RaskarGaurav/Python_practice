#!/usr/bin/python3

class MyList:
    def __init__(self,l):
        self.lst=l
    def __add__(self,other):
        tmp_ulst = self.lst.copy()
        for i in other.lst:
            if(i not in self.lst):
                tmp_ulst.append(i)
        return MyList(tmp_ulst)
    def __sub__(self,other):
        tmp_lst= []
        for j in self.lst:
            if(j not in other.lst):
                tmp_lst.append(j)
        for k in other.lst:
            if(k not in self.lst):
                tmp_lst.append(k)
        return MyList(tmp_lst)
a=[1,2,3,4]
b=[4,5,6,7]
l1= MyList(a)
l2= MyList(b)
subList= l1-l2
addList= l1+l2

print("l1+l2= ",addList.lst)
print("l1-l2= ",subList.lst)
