from collections import OrderedDict

# this function orderdcit() can put the data in an order that when the entry happen - if there is same item is inserting again then it won't change the position of item
l = OrderedDict()
bool = False
tl = []

try:

    for i in range(int(input())):
        t = []
        NP = input().split()
        if len(NP) > 1:
            temp = int(NP[len(NP) - 1])
            del NP[len(NP) - 1]
            s1 = ' '.join(NP)
            t.append(s1)
            t.append(temp)
            #print(t[0], t[1])


        if len(l)>0:
            for m, n in l.items():
                tl.append(m)
            if t[0] in tl:
                l[t[0]] = int(t[1]) + int(l[t[0]])
            else:
                l[t[0]] = int(t[1])

        else:
            l[t[0]] = int(t[1])
except StopIteration as e:
    print(e)

#print(l)
for m, n in l.items():
    print(m, n)


# Counter OrderedDict ************************************************
from collections import  Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ ==  '__main__':
    s = input()
    c = OrderedCounter(sorted(s))
    k = c.most_common(3)
    for m, n in k:
        print(m,n)

# ****** Finding Captian room
from collections import  Counter, OrderedDict

K = int(input())
R = input().split()

class OrderedCounter(Counter, OrderedDict):
    pass

c = OrderedCounter(R)
for i, j in c.items():
    if j == 1:
        print(i)
# input  5, 1 2 3 4 1 5 6 7  9 2 3 4 5 6 7 6 7 8   - Output - 8
