import numpy as np

# ******************************************   Floot(), Ceil(), Rint()
np.set_printoptions(sign=' ')  # print options of numpy
arr = np.array(list(map(float, input().split())))
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
# *********************************** Sum(), Prod()**************************
arr2 = []
n = list(map(int,input().split()))
for _ in range(n[0]):
    arr2.append(list(map(int, input().split())))
res = np.sum(arr2, axis=0)
print(arr2)
print(np.prod(res))

# ****************** Min(), Max() ************************************
arr3 = []
n = list(map(int,input().split()))
for _ in range(n[0]):
    arr3.append(list(map(int, input().split()[:n[1]])))

res = np.min(arr3, axis=1)
print(np.max(res))

# ********** mean(), var(), std() *******************************
np.set_printoptions(legacy='1.13')
arr4 = []
n = list(map(int,input().split()))
for _ in range(n[0]):
    arr4.append(list(map(int, input().split()[:n[1]])))
print(np.mean(arr4, axis=1))
print(np.var(arr4, axis=0))
print(np.std(arr4))

# **** dot(), cross() ****************************
A = []
B = []
n = int(input())
for _ in range(n):
    A.append(list(map(int, input().split()[:n])))
for _ in range(n):
    B.append(list(map(int, input().split()[:n])))
print(np.dot(A, B))

# ******** polyval(), polyint(), polyder(), polyval(), polyfit(), roots(), poly() *********************
A1 = list(map(float,input().split()))
print(np.polyval(A1, int(input())))

# ********* Add,sub.mul, div, mod,pow ******************************************************************
n, m = list(map(int, input().split()))
A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int, input().split())))
print(np.add(A,B))
print(np.subtract(A,B))
print(np.multiply(A,B))
print(np.floor_divide(A,B))
print(np.mod(A,B))
print(np.power(A,B))


### Take aray input from user ************************************************************
N, M, P = map(int, input().split())

ARR1 = []
ARR2 = []

for i in range(N):
        ARR1.append(list(map(int, input().split()[:P])))
for i in range(M):
        ARR2.append(list(map(int, input().split()[:P])))

ARR3 =  np.concatenate((ARR1,ARR2), axis=0)  # concatenating input arrays
print(ARR3)


#### prints zerso and ones
import numpy as np
N = tuple(map(int, input().split()))
print(np.zeros(N, dtype=int))
print(np.ones(N, dtype=int))
# input 3 3 3