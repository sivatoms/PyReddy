
import re

s = input()

ms = re.search(r'^a\w+', s)  # \A start of string
me = re.search(r'$a\w+', s)  # \Z End of a string

#p = re.search(input(), s)
#print(p.group(0))
#print(p.start())
#print(p.end())
print(ms.start())
print(me.end())
print(ms.group())




