n, m = map(int, input().split())

sp = list(map(int, input().split()))
res = []
ls = list(g for g in range(n))
if n == m:
    print(0)
else:
    try:

        for i in ls:
            kk = []
            for j in sp:
                kk.append(abs(j - i))
            res.append(min(kk))
        print(max(res))
    except:
        pass


# other simple solution
from math import  floor
n,m = map(int, input().split(' '))
c = sorted(map(int,input().split(' ')))
distances = [c[0]]  + [(((c[i] - c[i-1]))/2) for i in range(1, len(c))] + [(n-1-c[-1])]
try:
	print(floor(max(distances)))
except:
	print(0)


# input
# 5 2
# 0 4
 # output
 # 2

