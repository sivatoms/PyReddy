

def insertsort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[i]>lst[j+1]:
                lst[i],lst[j+1] = lst[j+1],lst[i]
                i = j +1
    return lst

def mlist(num):
    for i in range(num):
        c = int(input())
        lst.append(c)
    return lst

lst = []
num = int(input("enter the length of list : "))

lst = mlist(num)

result = insertsort(lst)

print(result)
