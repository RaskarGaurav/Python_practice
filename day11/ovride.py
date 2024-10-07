#!/usr/bin/python3

class dock:
    def __init__(self,n):
        self.var=n
    def __sub__(self,other):
        temp=self.var+"-"+other.var
        return dock(temp)

l1=dock("Hello")
l2=dock("World")
result=l1-l2
print(result.var)
