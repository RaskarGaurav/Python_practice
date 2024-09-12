#!/usr/bin/python3
import math

while(True):
    print("*****Scientific Calc*****")
    print("1. Power")
    print("2. Square Root")
    print("3. Logarithm")
    print("4. GCD")
    print("5. LCM")
    print("6.Exit")
    choice = int(input("Choice: "))
    if(choice==6):
        print("Exiting...")
        break
    else:
        n = int(input("Enter number: "))
        match choice:
            case 1:
                n1 = int(input("Enter exponent: "))
                print("Ans: ",n**n1,"\n")
            case 2:
                print("Ans: ",math.sqrt(n),"\n")
            case 3:
                print("Ans: ",math.log(n),"\n")
            case 4:
                n1 = int(input("Enter 2nd number: "))
                print("Ans: ",math.gcd(n,n1),"\n")
            case 5:
                n1 = int(input("Enter 2nd number: "))
                print("Ans: ",math.lcm(n,n1),"\n")
            case _:
                print("Ans: Undefined Input")

