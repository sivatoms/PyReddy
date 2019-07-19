from numpy import *

arr1 = array([ [2,3,4],[3,1,2] ])
arr2 = array([ [1,2,1],[3,1,2] ])
print(arr1+arr2)
#print(len(arr1))

lt = len(arr1)

for i in range(lt):
    arr1[i]=arr1[i]+arr2[i]
print(arr1)


