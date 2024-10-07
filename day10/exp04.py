#!/usr/bin/python3

try:
    with open('demo.txt','r') as f:
        contents=f.read()
except PermissionError:
    print("File do not have Permission.")
except:
    print("Something went wrong.")

else:
    print(contents)
