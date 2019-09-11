



n, k = map(int,input().strip().split(" "))
numbers = map(int,input().strip().split(" "))

counts = [0] * k
#print(counts)
for number in numbers:

    counts[number % k] += 1
    #print(counts)

count = min(counts[0], 1)
#print(k//2, k//2+1)
for i in range(1, k//2+1):
    if i != k - i:
        count += max(counts[i], counts[k-i])
        #print(counts[i], counts[k-i])
if k % 2 == 0:
    #print(k)
    count += 1
print(count)


# input
#15 7
#278 576 496 727 410 124 338 149 209 702 282 718 771 575 436

# OP- 11