from collections import  Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass

c = OrderedCounter(input() for i in range(int(input())))
print(len(c))
print(*c.values())

# Here Counter method remembers the number of entries made by dictionary and it's count
# OrderDict can sort the dictionary entries and overwrites if the element already exists




# this is another example
# This program finds the most common number in the given list and if any of them have same count in common then it will look for minim list number

from collections import  Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
n = int(input())
b = map(int, input().split()[:n])

c = OrderedCounter(b)
l = list(c.most_common())
#print(l)
#print(min(c.keys()))
#print(c.items(), max(c.values()))
res = list(l[0])
#print(res[0])

r = []
for i, j in l:
    if max(c.values()) == j:
        r.append(i)

print(min(r))


# input
# 11
# 1 2 3 4 5 4 3 2 1 3 4
# output
# 3    # here 3 and 4 numbers occurred 3 times but 3 is smaller than 4 so the answer is 3