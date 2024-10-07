#!/usr/bin/python3
import re

class MyPassString:
    def __init__(self,str):
        self.pas=str
    @staticmethod
    def checkPas(strng):
        x=re.search(r"(?=.*[a-zA-Z].*)(?=.*[0-9].*)",strng)
        if(len(strng)>=8 and x):
            return True
        else: return False
    def __mul__(self,other):
        if MyPassString.checkPas(self.pas):
            strg= self.pas+other.pas
            strg=("".join(sorted(strg)))
            return MyPassString(strg)
        else:
            return MyPassString("! Check Password...")
    def __truediv__(self,other):
        if MyPassString.checkPas(self.pas):
            strg=""
            st={'a','e','i','o','u','A','E','I','O','U'}
            for i in self.pas:
                if(i in st or i.isdigit()):
                    strg+=i
            for k in other.pas:
                if(k in st or k.isdigit()):
                    strg+=k
            return MyPassString(strg)
        else:
            return MyPassString("! Check Password...")

pas1=MyPassString("abcdefg8")
pas2=MyPassString("aefgipou125678")
newPas1= pas1*pas2
newPas2 = pas1/pas2

print("newpas1: ",newPas1.pas)
print("newpas2: ",newPas2.pas)
