
# Can create function without name -- which is Lambda-- And Functions Python are objects

def square(a):   ## This is usually the normal function
    return a*a

result = square(5)
print(result)


#### Lambda Function

f = lambda a : a * a   ## this can be used with only one expression such as a*a , a+b  , f is a ref obj
result = f(5)
print(result)   ## 