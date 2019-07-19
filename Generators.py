
# Generators will give you iterators - means object

def TopTen():

    yield 5  #  Yield here works as a iterator
    yield 6
    yield 7
values = TopTen()

print(values.__next__())
print(values.__next__())


def Topten1():

    n = 1
    while n <=10:
        sq = n*n

        yield sq
        n+=1
val2 = Topten1()

for i in val2:
    print(i)

n =3
def out(n):
    for i in range(n):
        return (i+1)

out(n)