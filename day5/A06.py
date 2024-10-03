#!/usr/bin/python3
str = "playing"

if(len(str)<3):
    print(str)
else:
    if(str[-3:]=="ing"):
        print(str[:-3]+'ly')
    else:
        print(str+'ing')
