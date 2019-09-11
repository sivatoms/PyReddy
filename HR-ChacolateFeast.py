
t = int(input())
for _ in range(t):
    n, c, m = map(int, input().split())
    temp = n//c
    wr = temp
    while wr >= m:
        temp += wr//m
        wr = wr//m+wr % m
    print(temp)

# 1
# 43203 60 5

# output
# 899