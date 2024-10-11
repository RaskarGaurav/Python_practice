#!/usr/bin/python3

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print(people)
print({i:people[i] for i in sorted(people.keys())})

