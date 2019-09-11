n = int(input())
s = list(map(int,input().split()[:n]))
d, m = map(int, input().split())
r = 0

for i in range(0,n):
    print('S value is : ',s[i],'+',s[:i+m],s[i:i+m], 'i value : ', i, 'm value : ', m)
    if sum(s[i:m+i]) == d:      #  here s[i:i+m] creates consecutive pairs and their sum
        r += 1
    else:
        r += 0
print(r)


# input
# 5
# 1 2 1 3 2
# 3 2  # d is 3, m is 2    , day and month




