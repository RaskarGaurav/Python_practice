#!/usr/bin/python3

import math

while(True):
    print("*****MEnU*****")
    print("1. add")
    print("2. subtract")
    print("3. Multiply")
    print("4. integer division")
    print("5. modulo")
    print("6. equals")
    print("7. power")
    print("8. square root")
    print("9. logarithm")
    print("10. GCD/HCF")
    print("11. LCM")
    print("12. Exit")
    choice = int(input("Choice: "))
    if(choice==12):
        print("Exiting...")
        break
    else:
        n1 = int(input("Enter first Number: "))
        n2 = int(input("Enter seconf Number: "))
        print("Ans: ")
        match choice:
            case 1:
                print(n1+n2)
            case 2:
                print(n1-n2)
            case 3:
                print(n1*n2)
            case 4:
                print(n1//n2)
            case 5:
                print(n1%n2)
            case 6:
                print("Equal" if(n1==n2) else "Not Equal")
            case 7:
                print(n1**n2)
            case 8:
                print(math.sqrt(n1)," and ",math.sqrt(n2))
            case 9:
                print(math.log(n1)," and ",math.log(n2))
            case 10:
                print(math.gcd(n1,n2))
            case 11:
                print(math.lcm(n1,n2))
            case _:
                print("Undified Input")












