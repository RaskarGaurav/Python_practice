#!/usr/bin/python3

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print(people)
print("Total people: ",len(people))

people['Lisa']='Black'
print(people)
people.pop('Jenny')
print(people)
