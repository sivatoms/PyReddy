
def update(x):
    x = 10
    #print("x is :", x)

a = 8
update(a)
#print(a)


### Update a list without changing the address

def update_lst(lst):

    print(id(lst))
    lst[1] = 40
    print(id(lst))
    print("lst is : ",lst)

lst = [10,20,30]
print(id(lst))
update_lst(lst)
print("lst is : ",lst)
