from collections import  Counter
import re
g = int(input())

for _ in range(g):
    n = int(input())
    s = input()
    l = list(s)
    if '_' not in l:
        if len(l) == 1:
            print('NO')
        else:
            for i in range(len(l) - 1):
                if l[i] == l[i + 1]:
                    #print(i, i+1,l[i], l[i+1])
                    bool = True
                else:
                    if bool:
                        bool = False
                    else:
                        bool = False
                        break

            #print(bool)
            if bool:
                print('YES')
            else:
                print('NO')
    else:
        if re.search(r'^_+$', s):
            print('YES')
        else:
            r1 = list([k for k in l if k != '_'])
            res = list(Counter(r1).values())
            #print(res)
            #print(list(k2 for k2 in res.values()))
            if min(res) > 1:
                print('YES')
            else:
                print('NO')
''''
#input
4
7
RBY_YBR
6
X_Y__X
2
__
6
B_RRBR

output
YES
NO
YES
YES
'''