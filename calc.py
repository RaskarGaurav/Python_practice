#!/usr/bin/python3

while True:
    print("*****MEnU*****")
    print("1.add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    try:
        ch=int(input("Choice: "))
    except ValueError:
        print("Give Integer Input.\n")
        continue
    except:
        print("Your Facing Exception.\n")
        continue

    if(ch==5):
        print("Exiting...\n")
        break
    l=[1,2,3,4]
    if(ch not in l):
        print("Choose Correct Option.\n")
        continue
    try:
        a=int(input())
        b=int(input())
    except ValueError:
        print("Give Integer Input.\n")
        continue
    except:
        print("Your Facing Exception.\n")
        continue

    match ch:
        case 1:
            print("Ans:",a+b)
        case 2:
            print("Ans:",a-b)
        case 3:
            print("Ans:",a*b)
        case 4:
            print("Ans:")
            try:
                print(a/b)
            except ZeroDivisionError:
                print(0,"\n\nIndeterminant format.Default Zero.\n")
        case _:
            print("Something went wrong...\n")
