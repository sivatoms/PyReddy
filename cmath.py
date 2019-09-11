from cmath import phase, polar
from math import sqrt
import re

s = input()
# polar, complex
print(*polar(complex(input())), sep ='\n')



x = re.search(r'(^[0-9])+', s)
k = re.search(r'.\+.', s)

k = k.group().replace('+','')
l = list(k)
l1 = int(l[0]) * int(l[0])
l2 = int(l[1]) * int(l[1])

res = sqrt(l1+l2)
print(res)
#second line
print(phase(complex(s)))

