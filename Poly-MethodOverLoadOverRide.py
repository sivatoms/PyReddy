
# MethodOverLoading

class A():

    def sum(self,a=None,b=None,c=None):

        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s =a + b

        else:
            s =a
        return s

s1 = A()

print(s1.sum(3, 4))

#MethodOverRiding

class A():
    def Show(self):
        print("in A Show")

class B(A):
    pass            # this method can get parent method Show without having any method in it

class C(A):     # This class has overridig method Show() of A() class
    def Show(self):
        print("in C Show")
a1 = A()
b1 = B()
c1 = C()
print(c1.Show())
