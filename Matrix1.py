from numpy import *

arr = array([   [1,2,3,4],
                [5,6,7,8]
            ])
#print(arr)

m = matrix([ [1,2,4],[5,3,6]])  # int float
m1 = matrix('1,2;3,4')
m2 = matrix('1,2;3,4')   # string elements
#print(m)
#print(m2)

m3 = matrix([[1,2,3],[4,5,6],[7,8,9]])
print(diagonal(m3))    # diagonal elements
print(m.max())  # max element
print(m.min())  # min element
print(m1*m2)    # multiplication
