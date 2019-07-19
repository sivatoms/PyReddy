from numpy import *
##apend a value to array
arr = array([1,2,3,4,90])
arr = arr +0
print(arr)
## adding two arrays
arr2 = array([6,5,7,8,9])
arr3 = arr + arr2
print(arr3)

print(min(arr))
print(sum(arr))
print(sin(arr))
print(sort(arr2))

#copying array
arr3 = arr2
print(arr3,arr2)
print(id(arr3))
print(id(arr2))

#copying array with different address
arr3 = arr2.view() # view function will help you to create new array
arr3 = arr2.copy()  # copy will give deep copy without referencing shallow copy like view func