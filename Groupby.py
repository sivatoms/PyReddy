from itertools import groupby

l = [list(g) for k, g in groupby(input())]   #   AAAABBBCCD
l2 = [''.join(i) for i in l]

for i in range(len(l2)):
    if len(l2[i])==1:
        print('(1, '+l2[i]+')',end='')
    else:
        t = l2[i]
        print('('+str(len(l2[i]))+', '+t[0]+')',end='')