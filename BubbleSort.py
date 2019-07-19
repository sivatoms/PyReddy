
def bubble(lst2):
    l = len(lst2)
    for i in range(l-1, 0, -1):
        for j in range(i):
            if lst2[j] > lst2[j+1]:
                lst2[j], lst2[j+1] = lst2[j+1], lst2[j]
                #bubble(lst2)
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