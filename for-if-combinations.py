from itertools import groupby,combinations
n = int(input())
s = list(input().split())
k = int(input())

le = len(list(combinations(s, 2)))
l1 = list(combinations(s, k))  # this is a list
f = [i for i in l1 if 'a' in i]   #  this is to check if i has any 'a' in it.----> usefule for many oteration purpose
print("%.4f"% (len(f)/len(l1)))

