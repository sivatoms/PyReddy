n1 = int(input())
s1 = set(input().split()[:n1])
#print(s1)
n2 = int(input())

s2 = set()
for i in range(n2):
    for j in range(1):
        if j == 0:
            temp = input().split()
            s2 = set(input().split()[:int(temp[1])])
            eval('s1.{0} ({1})'.format(temp[0], s2))
res = 0
for sm in s1:
    res += int(sm)

print(res)





