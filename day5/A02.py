#!/usr/bin/python3
str = "restart"
u = str[0]
str = str[1::].replace(u,"$")
print(u+str)

str1 = "restart"
str2 = ""
k = str1[0]
for i in str1[1:]:
    if(i==k):
        str2 = str2+'$'
    else:
        str2 = str2+i
else:
    str2 = k + str2
print(str2)
