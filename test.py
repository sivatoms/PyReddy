
S = input()
k = input()
import re
pattern = re.compile(k)

#print(pattern)
#r = pattern.search(S)
r = re.search(k,S)
if not r: print( "(-1, -1)")
while r:

    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)
    #r = re.search(k, r.start()+1)



pattern = re.compile("d")
pattern.search("dog")     # Match at index 0
pattern.search("dog", 0)  # No match; search doesn't include the "d"