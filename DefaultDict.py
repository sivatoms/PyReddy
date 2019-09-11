from collections import defaultdict

n, m = map(int, input().split())
a1 = defaultdict(list)
b1 = []
for i in range(0, n):
    a1[input()].append(i+1)   # here the input beacomes the word and appedn will tell how many times that word is entered into the dict
for _ in range(m):
    b1.append(input())
print(a1)

for i in b1:
    print(i)
    if i in a1:
        #print(" ".join(map(str, i)))
        print(a1[i])
    else:
        print(-1)


#   input *******
#5 2
#a
#a
#b
#a
#b
#a
#b