import time
# Bubble Sort compare each element with the next element to it in an array
start_time = time.time()
def bubble(lst2):
    l = len(lst2)
    for i in range(l):
        flag = False
        for j in range(l-1):
            #print('first: ',lst2[j], lst2[j+1])
            if lst2[j] > lst2[j+1]:
                lst2[j], lst2[j+1] = lst2[j+1], lst2[j]
                flag = True
                #bubble(lst2)
            #print('second',lst2[j], lst2[j + 1])
        #print()
        if not flag:
            break
    return lst2

def mlist(num):
    for i in range(1, num+1):
        c = int(input())
        lst1.append(c)
    return lst1

lst1 = []
num = int(input("Enter the length of the list : "))

lst2 = mlist(num)
print(lst2)

result = bubble(lst2)

print("The bubble sorted array is : ", result)

end_time = time.time()
total_time = end_time - start_time
print('Total time took to run the bubble sort is :', total_time)
# time complexity is O(n2)
# space Complexity is O(1)