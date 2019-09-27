
##  Difference between sums of Left Diagnal and Right Diagnal of matrix

# 00 01 02
# 10 11 12
# 20 21 22

# 02 01 00
# 12 11 10
# 22 21 20

def compareTriplets(a):

    LD = 0
    RD = 0
    b = []

    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                LD += a[i][j]

    for i in range(len(a)):
        s = a[i]
        s = s[::-1]
        b.append(s)

    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                RD += b[i][j]

    return abs(LD-RD)


n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = compareTriplets(arr)
print(result)