n = int(input())
a = []
for j in range(1, n+1):
    a.append(j)
#print(a)

#a = [1,2,3,4,5]
b = [1,6,16,31,51]
res = 0
for i in range(len(b)-1):
    res += abs(b[i]-b[i+1])
    #print(a[i]+1,' == > ', res+1)

k = 0
c = 0
for i in range(n):
    #print(i, a[i])
    if a[i] == 1:
        k = 1
    elif a[i] == 2:
        k += 5
    else:
        if a[i]>2:
            k += 10 + c
            c += 5

    #print(a[i], k)
    #print('---------------')
print(k)
