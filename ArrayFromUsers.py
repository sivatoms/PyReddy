from array import *

arr = array('i', [])
n = int(input('enter the length of the array : '))
for i in range(n):
    x = int(input('enter the next value : '))
    arr.append(x)
print(arr)

val = int(input('enter the value for search : '))
#finding index of an element
k=0
for e in arr:
    if e == val:
        print(k)
        break
    k+=14

print(arr.index(val))
