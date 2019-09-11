
from itertools import permutations

a1, r = input().split()
print(*[''.join(i) for i in permutations(sorted(a1),int(r))],sep='\n')   # here * will unpack list and print them line by line

def sum(*l):
    result = 0
    for i in l:
        result += i
    print(result)
sum(1,2,3,4)

