#!/usr/bin/python3

def entr(k):
    while True:
        nme=input("Enter Name: ")
        if(k and nme in d1):
            print("\nalready exist...")
            continue
        vh=input("Enter vehicle: ")
        d1[nme]=vh
        print("\nSuccessfully operated\n")
        opt=input("next entry? y/n: ")
        if(opt!="y"): break

def dele(nme):
    if (nme not in d1): print("\ndo not exists...\n")
    else:
        print("(",nme,"-",d1[nme],")-> Do u really want to delete?y/n: ")
        opt=input()
        if(opt=="y"):
            d1.pop(nme)
            print("\nSuccessfully operated\n")
def srch():
    ls=list(x for x in input("Enter name/names to search: ").split())
    for i in ls:
        if(i in d1): print(i,"-",d1[i])
        else: print(i,"- ------")
    print("\nSuccessfully operated")

d1={}
opts={"a","b","c","d","e","f","g"}
while True:
    print("*****MEnU*****")
    print("a. Add name & vehicle",
         "\nb. Delete the vehicle entry",
         "\nc. Modify vehicle entry",
         "\nd. Search vehicle entry",
         "\ne. Search list of vehivle entry",
         "\nf. Display all person names",
         "\ng. Display all vehicle names",
         "\nh. Exit")
    n= input("\n***Choice: ")
    if(n=="h"): break
    elif(n not in opts):
        print("\nEnter correct option...\n\n")
        continue

    match n:
        case "a":
            print("\n**New Entry**")
            k=True
            entr(k)
        case "b":
            nme=input("Enter name to delete entry: ")
            dele(nme)
        case "c":
            print("\n**Modify Entry**")
            k=False
            entr(k)
        case "d"|"e":
            srch()
        case "f":
            print("\nPeople = ",d1.keys(),"\n")
        case "g":
            print("\nVehicles = ",set(d1.values()),"\n")
        case _:
            print("Mastiiii ;-)")

print(d1)
