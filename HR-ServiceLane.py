n, t = map(int, input().split())
w = list(map(int, input().split()))
for _ in range(t):
    i, j = map(int, input().split())
    print(min(w[i:j+1]))

# input
# 8 5
# 2 3 1 2 3 2 3 3
# 0 3
# o/p 1
# 4 6
# o/p 2
# 6 7
# o/p 3
# 3 5
# o/p 2
# 0 7
# o/p 1