


r, c = input().split()

#c = 27
rows = int(int(r)/2)
columns = (int(int(c)/2) + 1)
k =2
#print(rows, columns)

print(int((columns-7)/2))
# top 4 rows part
for i in range(rows):
    c2 = columns - k
    for j in range(columns-k):
        print('-', end='')
    k += 3
    if i ==0:
        print('.|.',end='')
    else:
        for l1 in range(i+1):
            print('.|.', end='')
        for l2 in range(i):
            print('.|.', end='')

    for m in range(c2):  # 14 -3 = 12
        print('-', end='')
    print()
# WELCOME PART
for i in range(int((int(c)-7)/2)):
    print('-', end='')
print('WELCOME', end='')
for j in range(int((int(c)-7)/2)):
    print('-', end='')

# BOTTOM SECTIONS REVERSE OF TOP

print()
k1 = 3
k2 = 3
b = 6
for i in range(rows):
    for j in range(k1):
        print('-', end='')
    k1 += 3
    if i == 0:
        for j in range(int((int(c) - b) / 3)):
            print('.|.', end='')
            #b += 6
    else:
        b +=6
        for t in range(int((int(c) - b) / 3)):
            print('.|.', end='')


    for j2 in range(k2):
        print('-', end='')
    k2 += 3
    print()





# **** Design pattern using string slicing ######
import string
n = int(input())
lst = []
for i in range(n):
    s = "-".join(string.ascii_lowercase[i:n])
    lst.append((s[::-1] +s[1:]).center(4*n-3, "-"))
print('\n'.join(lst[:0:-1]+lst))
