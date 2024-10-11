#!/usr/bin/python3

ls=[j for j in input().split()]
word_count = {}
for i in ls:
    word_count[i]=word_count[i]+1 if(i in word_count) else 1

suffix_count={'s':0,'es':0,'ed':0,'y':0,'en':0}
for i in ls:
    if(i.endswith("es")): suffix_count['es']+=1
    elif(i.endswith("s")): suffix_count['s']+=1
    elif(i.endswith("ed")): suffix_count['ed']+=1
    elif(i.endswith("y")): suffix_count['y']+=1
    elif(i.endswith("en")): suffix_count['en']+=1

word_length_count={}
for i in ls:
    word_length_count[len(i)]=word_length_count[len(i)]+1 if(len(i) in word_length_count) else 1

print("word_count= ",word_count)
print("suffix_count= ",suffix_count)
print("word_count_length= ",word_length_count)

