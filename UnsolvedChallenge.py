inp = list(input().split())

arr = list(input().split())
setA = set(input().split())
setB = set(input().split())

t1 = (i in setA for i in arr)
t2 = (i in setB for i in arr)

res1 = 0
res2 = 0

#if inp[0] == len(arr) and inp[1] == len(list(setA)) and inp[1] == len(list(setB)):

for i in range(len(arr)):
    if next(t1) == True:
        #print(i)
        res1 += 1


for i in range(len(arr)):
    if next(t2) == True:
        #print(i)
        res2 += 1


print(abs(res1-res2))

#if inp[0] == len(arr) and inp[1] == len(list(setA)) and inp[1] == len(list(setB)):
  #  res1 = len(list(setA.intersection(set(arr))))
  #  res2 = len(list(setB.intersection(set(arr))))
  #  print(abs(res1-res2))

# thsi code worked on hacker rank - i dont know why my code did not
n, m = raw_input().split()

sc_ar = raw_input().split()

A = set(raw_input().split())
B = set(raw_input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))