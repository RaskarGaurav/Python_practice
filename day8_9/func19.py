#!/usr/bin/python3

def isPrime(n):
    i=2
    while(n>=i*i):
        if(n%i==0): return False
        i+=1
    return True
def sfIn():
    while True:
        try:
            n=int(input("Input: "))
            if(n<=0):
                print("Enter +ve Integer.")
                continue
            return n
        except ValueError:
            print("Enter Correct Input")

num=sfIn()
print(isPrime(num))
