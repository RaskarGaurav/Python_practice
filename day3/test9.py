#!/usr/bin/python3


while(True):
    print(format("Menu",'*^5'))
    print("1. Binary")
    print("2. Octal")
    print("3. Hexa Decimal")
    print("4. Exit")
    choice = int(input("Choice: "))
    if(choice==4): break
    else:
        n = input("Input: ")
        match choice:
            case 1:
                print("Integer: ",int(n,2))
            case 2:
                print("Integer: ",int(n,8))
            case 3:
                print("Integer: ",int(n,16))
            case _:
                print("Integer: Wrong Input")

