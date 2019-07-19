
# inheritance are 3 types - single , multi level adnd multiple inheritance

class A():  #super class

    def feature1(self):
        print("Feature 1 is working ")

    def feature2(self):
        print("Feature 2 is working ")


class B(A):     # B is a sub class which inherites all features from Class A  -- sibgle inheritance

    def feature3(self):
        print("Feature 3 is working ")

class C(B):         # Multi level inheritance

    def feature4(self):
        print("Feature 4 is working ")

class D():

    def feature5(self):
        print("Feature 5s is working ")


class E(A, D):  # multiple inheritance

    def feature6(self):
        print("Feature 6 is working ")


a1 = A()

a1.feature1()
b1 = B()
b1.feature1()

c1 = C()
c1.feature3()

