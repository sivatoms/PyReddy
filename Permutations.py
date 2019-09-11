from itertools import permutations

a1, r = input().split()
print(*[''.join(i) for i in permutations(sorted(a1),int(r))],sep='\n')

