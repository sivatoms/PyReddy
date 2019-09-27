

# KasperConstant  - descend num -  ascend num == 6174
n = input()
t = sorted(n)
t = ''.join(i for i in t)
t1 = t[::-1]
counter = 0
while int(t1)-int(t) != 6174:
    k1 = (int(t1)-int(t))
    if k1<1000:
        k1 = str(k1)+'0'
        #break
    k2 = sorted(str(k1))
    k3 = ''.join(i for i in k2)
    k4 = k3[::-1]
    t1 = k4
    t = k3
    #print(k3, k3[::-1])
    #break
    counter += 1
    #print(k1)

print(counter+1)

# input 2111
# output 5




