import operator
from functools import reduce

nM = int(input())
M = set()
a = input()
ml = a.split()
mlist = list(map(int, ml))
for i in mlist:
    M.add(i)


nN = int(input())
N = set()
b = input()
nl = b.split()
nlist = list(map(int, nl))
for i in nlist:
    N.add(i)

#print(M)
#print(N)

res = []

#print(M.difference(N))
#print(N.difference(M))

res.append(list(M.difference(N)))
res.append(list(N.difference(M)))

f = reduce(operator.concat, res)   # reduce can be used to flat the lists from sublists

#print(res)
result = sorted(f)
for i in range(len(f)):
    print(result[i])


# Challenge 2 on sets
#n = int(input())
#a = set()
#a.add('Trinidad & Tobago,')
#for i in range(7):
   # a.add(input())
#print(len(list(a)))
#print(a)

# single line execution of len of unique elements in a set
print(len(set(str(input()) for i in range(int(input())))))
