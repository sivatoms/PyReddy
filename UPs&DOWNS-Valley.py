# books problem
# counting number of pages you have to turn when you want to get to page p from backside or front side


n = int(input())
s = list(input()[:n])
#   pair for n numbers   =  [(1), (2,3),(4,5)),(6,7),(8)]
v = 0

#for j in range(len(s)//2):
u = 0
d = 0
for i in s:
    if i == 'U':
        u += 1
    else:
        u -= 1
    print(u, i)
    if u == 0 and i == 'U':   #here where the one valley completes
        v += 1
print(v)
print(s)

#print(n//2)
#           /\
# \  /\    /
#  \/  \/\/
#input
#6
#DDUDUU