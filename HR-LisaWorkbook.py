n, k = map(int, input().split())
c = list(map(int, input().split()))

count = 0
page = 1

for i in c:
    for j in range(1, i + 1):
        if page == j:
            count = count + 1
        if (j % k == 0) or (j == i):

            page = page + 1

print(count)

# 10 5
# 3 8 15 11 14 1 9 2 24 31

# 8