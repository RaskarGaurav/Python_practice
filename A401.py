#!/usr/bin/python3

while(True):
    print("*****MEnU*****")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Integer Divison")
    print("5. Exit")
    choice = int(input("Choice: "))
    if(choice==5):
        print("Exiting...")
        break
    else:
        n1 = int(input("Enter 1st number: "))
        n2 = int(input("Enter 2nd number:"))
        print("Ans: ")
        match choice:
            case 1:
                print(n1+n2,"\n")
            case 2:
                print(n1-n2,"\n")
            case 3:
                print(n1*n2,"\n")
            case 4:
                print(n1//n2,"\n")
            case _:
                print("Undefined Input")



