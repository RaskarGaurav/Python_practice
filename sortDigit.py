ls=[10,20,30,55,1,2,78,11,22]

sls= sorted(ls, key= (lambda x: x%10))
print(ls)
print(sls)
