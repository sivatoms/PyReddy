

# Iterator are two methods --  iter() , next()
# iter() method wil give you object and next() method wil give you next value.

num = [7,8,9,12]
print(num[3])

it = iter(num)

print(it.__next__()) #  prints the next value from a list

# creating own iteratros

class TopTen():

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num+=1
        else:
            raise StopIteration

        return val

t = TopTen()

print(t.__next__())
for i in t:
    print(i)

