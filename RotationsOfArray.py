n, k, q = map(int, input().split())

a = list(map(int, input().split()[:n]))


res = []
for i in range(q):
    i = int(input())
    res.append(a[i - k % n])  # I DONT KNOW HOW SOMEONE THINK OF THIS WAY OF SOLVING THE PROBLEM

for e in res:
    print(e)


# INPUT
# 3 2 3 # HERE N=3, K=2, Q=3 --- N IS LEN OF ARRAY, K IS NUMBER OF ROTATIONS, Q IS THE INDEX POSITIONS OF ELEMESTS TO PRINT AFTER ALL ROTATIONS
# 1 2 3
# 0
# 1
# 2
