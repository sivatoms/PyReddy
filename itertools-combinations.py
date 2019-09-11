from itertools import combinations, combinations_with_replacement

def combi(s, k):

    for l in range(1, k+1):
        print(*[''.join(i) for i in combinations(sorted(s), l)], sep='\n')

s, k = input().split()
combi(s, int(k))



# itertools combinations with replacement


def combi_w_repl(s, k):

    print(*[''.join(i) for i in combinations_with_replacement(sorted(s), k)], sep='\n')

s, k = input().split()
#combi(s, int(k))   # this one is just combinations of first function combi
combi_w_repl(s, int(k))


#   type in output-    HACK 2


# Allows us to create distinct pairs from a single list
l = [10,20,30]
r = 0
for i in combinations(l, 2):  # which creates distinct tuple combinations from a single list and the second parameter in the combinations is 2 means (1,2) pair(2)
    r += abs(i[0]-i[1])
print(r)


# Another example
### check pairs sum is divisible by given number k and the count of them

from itertools import combinations
n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()[:n]))
counter = 0
res = (counter+1 for i in combinations(a, 2) if sum(list(i))%k == 0)
print(sum(counter+1 for i in combinations(a, 2) if sum(list(i))%k == 0))


# input
# 6 3
# 1 3 2 6 1 2
# output
# 5




# this is anorher way of getting unique pairs from a list
n = int(input())
rq, cq = map(int, input().strip().split())

RL = []
#R.append(list((i,j) for i in range(1,rc+1) for j in range(1,cq+1) if i>1 or j>1))
RL.append(list((rq, j) for j in range(1, n+1)))
for i in RL:
    print(i)
