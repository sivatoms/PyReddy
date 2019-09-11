
from itertools import product

k, md = map(int, input().split())
r = 0
l = [list(map(int, input().split()[1:])) for _ in range(k)]   # using single line with for loop and taking multiple line of lists into one

res = map(lambda x: sum(i**2 for i in x) % md, product(*l))   # using cartesian product and more advanced of using lambda here x fetch the value (sub-list)
                                                              # from product(list(which has sub-lists)) and it will do the pow() and sum % md - finally create a lists of sums
print(res, max(res))


# example of map and lambdsa

L = [1, 2, 3, 4]
k = list(map(lambda x: x**2, L))
print(k)   # will give you ...   [1, 4, 9, 16]