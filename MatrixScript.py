# Decoding matrix script into "This$#is% Matrix# %!"
import re
n = list(map(int, input().split()))

#print(n)
l1 = []

for i in range(n[0]):
    #for j in range(n[1]):
    l1.append(input())
#print(l1)
res = []
t = ''
t2 = ''
t3 = ''
st = ''
for i in range(n[0]):
    t1 = list(l1[i])

    j = 1
    for k in range(j):
        res.append(t1[k])
        t = t+t1[k]
        del t1[k]
        t2 = t2+t1[k]
        t3 = t3+t1[k+1]


#print(res)
#print(l1)
temp = t+t2+t3
#temp = 'this$#is% Matrix#  %!'

#print(re.sub(r'[\$|\#|\%].(\#|\$|\!|\s|\%)', ' \1', temp))
#temp2 = re.sub(r'(\$|\#|\%|!)', '\1', temp)
#print(temp2)
#print(re.sub(r'(\$|\#|\%|!).', ' \1', temp))




a = re.sub(r'([$#%!\s]+?)$', ' ', temp)
t = re.search(r'([$#%!\s]+?)$', temp)
#print(type(a))
k = t.group()
#print(k)

temp2 = re.sub(r'(\$|\#|\%|!)', ' ', temp)
#print(temp2)
fr = re.sub(r'\s+', ' ', temp2)
print(fr.rstrip()+''+k.lstrip())
#print(t2)
#print(t3)



# # i#
#  @#U


import re

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))




#  ********* ANOTHER SOLUTION FOR ALL TEST CASES

n, m = map(int, input().split())
a, b = [], ""
for _ in range(n):
    a.append(input())
#print(a)
i = 0
for z in zip(*a):

    b += "".join(z)
   # print(b,'-->', i)
    i+=1
#print(b, 'Final')
#print('****************************************')
#print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', b))

print(re.findall(r'\bis', 'This island is beautiful'))
