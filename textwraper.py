import textwrap

# one more method textwrap.wrap()
# my method
def wrap(a,n):
    print(textwrap.fill(a, n))
    l = list(a)
    k = ''
    if len(l)>= n:
        for j in range(round((len(a)/n))):
            t = 0
            for i in range(n):
                k = k+l[t]
                del l[t]
            k = k+'\n'

    if len(l)<n:
        for i in range(len(l)):
            k = k+l[i]
    print(l)
    return k

# library method
def wrap1(a, n):
    return textwrap.fill(a, n)


a = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
n = 4
result = wrap1(a, n)
print(result)