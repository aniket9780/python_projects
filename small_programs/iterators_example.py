from itertools import *

persons = [{'name':'Tim','age':25},{'name':'Tom','age':25},
           {'name':'Danny','age':29},{'name':'Harry','age':65}]
a = [1,2,9,4,5]
b = [3,4]
prod = product(a,b)
print(list(prod))

per = permutations(a,2)
print(list(per))

comb = combinations(a,2)
print(list(comb))

comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

acc = accumulate(a ,func=max)
print(list(acc))

grp =  groupby(persons,key=lambda x: x['age'])
for key,values in  grp:
    print(key, list(values))


