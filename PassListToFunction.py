
### This program pass a list to a function as a parameter and it retunrs multiple values like count of odd and even in the list
even = []
odd = []
lst = []
l = int(input("enter length of list ; "))
#Take list from a input user : -
for i in range(l):
    #lst = lst.append(int(input()))
    print("Enter list values in odd and even - " )
    num = int(input())
    lst.append(num)
    #print(lst)
   # print(num)

def passlist(lst):
    for j in lst:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
    return even,odd

even,odd = passlist(lst)
print(lst)
print(even)
print(odd)

#print(e,o)
print("Even : {} and Odd : {}".format(even,odd))
