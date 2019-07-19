
# using normal logic
def fact(f):
    a = 1
    for i in range(1,f+1):
        a = i * a
    return a

f = 6
result = fact(f)

print(result)

# using recursion logic

def fact2(n):
    if n==0:
        return 1
    return n * fact2(n-1)

resul = fact2(5)

print(resul)
