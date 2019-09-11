import numpy as np

n = int(input())
arr = np.array([])
arr = np.array([input().split() for i in range(n)], float)   # inserting multi dimensional array using input
np.set_printoptions(legacy='1.13')
print(np.linalg.det(arr))


#  One line solution - Brilliant
print(round(np.linalg.det(np.array([input().split() for _ in range(int(input()))], float)), 2))