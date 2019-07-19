from numpy import *

arr1 = array([34,100,501,69])
i = 0
j = 0
for i in range(len(arr1)):
    for j in range(len(arr1)):
        if arr1[i] < arr1[j]:  #  >  for maximum value
            temp = arr1[j]
            arr1[j] = arr1[i]
            arr1[i] = temp
print(arr1[0])
print(arr1)