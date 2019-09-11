# Set A is said to be subste of B. if all elements of A are in B.

T = int(input())

for i in range(T):
    for j in range(1):
        t1 = int(input())
        s1 = set(input().split()[:t1])

    for m in range(1):
        t2 = int(input())
        s2 = set(input().split()[:t2])

    print(s1.issubset(s2))




