from numpy import *

arr =  array([ [1,2,3,6,2,9], [4,5,6,7,5,3] ])
print(arr.dtype)  # data type
print(arr.ndim)   # gives rank of array
print(arr.shape)  # columns nd rows count
print(arr.size)   # size of an array

arr2 = arr.flatten() # converts multi to single dim array
print(arr2)

arr3 = arr2.reshape(3,4)  # convert array 3d array
arr4 = arr2.reshape(2,2,3) # 2 arrays 2/3 array
print(arr3)
print(arr4)