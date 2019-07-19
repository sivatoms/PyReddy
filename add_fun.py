
def add_sub(x, y):
    c = x + y
    d = x - y
    return c,d
add_sub(4, 5)

res = add_sub(6,3)
print(res)
res1 , res2 = add_sub(5,4)
#print(res1,res2)

def person(name,age):   # position argument
    print(name)
    print(age)
person("Shiva",27)

def person2(name,age):   # keyword argument argument
    print(name)
    print(age)
person2(age=27, name = 'Shiva')

def person3(name,age  = 18):   # default  argument
    print(name)
    print(age)

person3("Shiva")

def sum(a,*b):   # variable length argument -- *b means it can take multiple values
    c = a
    for i  in b:
        c = c + i
    print(c)
    print(a)
    print(b)
    #print(c)
#sum(5,6,1,3)

def person(name,**data):   #-- two  *   to print variable length argumaents
    print(name)
    for i,j in data.items():   ### i, j are value and name -- pair --> city - i and j-> toronto
        print(i,j)
    print(data)
person('shiva',age=28,city='toronto',mobile=647787)






