
# find the min or max from list and sort accordingly
def selectsort(lst2):

   for i in range(len(lst2)-1):
       minpos = i
       for j in range(i, len(lst2)):
           if lst2[j] < lst2[minpos]:
               minpos = j

       lst2[i], lst2[minpos] = lst2[minpos], lst2[i]  # swaping happens in the outer loop so the workload will eventually reduce better than bubble sort
       print(lst2)

   return lst2

def mlist(num):
    for i in range(num):
        c = int(input())
        lst.append(c)
    return lst

lst = []
num = int(input("Enter length of a Selection Sort : "))

lst2 = mlist(num)
print(lst2)
result = selectsort(lst2)
print("The Select Sorted List is :  ",result)

