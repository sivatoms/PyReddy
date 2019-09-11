import re

#  cpaitalize first letter in a giver string -- using capitalize function

st = input()

def solve(s):
    st = s.split(' ')
    res = ' '.join(word.capitalize() for word in st)
    return res

r = solve(st)
print(r)




## example  -    hello  world lol     o/p   Hello  World Lol