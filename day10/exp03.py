#!/usr/bin/python3
try:
    with open('exp.py','r') as f:
        contents=f.read()
except FileNotFoundError:
    print("File not found")
except:
    print("Something wrong")
else:
    print(contents)
