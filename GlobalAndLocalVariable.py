a = 10

print(id(a))  # gives ou address
def something():

   # 1.  global a  # hardcoding saying a is global and it returns only one global variable -- and you can not access it as local
    a = 9
    x = globals() ['a'] ### we can access all global variables
    print(id(x))

    print("local variable a : ", a)
    globals()['a'] = 20   # this will not effect loacal variable
something()

print("Global Variable a :", a)