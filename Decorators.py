
# Decorators can be used to reshape the functions- you can use functions inside the functions :

def div(a,b):
    print(a/b)

def smart_div(func):   ## callig function func - which is div - we can pass functions as argument in decorators

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,4)