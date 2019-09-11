
# Picking Numbers    - unsolved

n=int(input())
l=[int(i) for i in input().split()]
maximum=0
for i in l:
    print('i only  ... ', l.count(i),'  i :', i,'\n')
    print('i-1     ....', l.count(i-1) ,'  i-1 :', i-1,'\n')
    print('------------------------------------------------')
    c=l.count(i)
    d=l.count(i-1)
    c=c+d
    if c > maximum:
        maximum=c
print(maximum)

# input
#6
#4 6 5 3 3 1

# out put is 3


# problem

#Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to . For example, if your array is , you can create two subarrays meeting the criterion:  and . The maximum length subarray has  elements.