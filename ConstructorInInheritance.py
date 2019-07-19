

class A:

    def __init__(self):
        print("Constructor __init__ A")

    def feature1(self):
        print("Feature 1 is working ")

    def feature2(self):
        print("Feature 2 is working ")

class B(A):  # B is a sub class which inherites all features from Class A  -- sibgle inheritance

    def __init__(self):
        #super().__init__()
        print("constructor __init__ B")    # when B is child of A and B has it's own __init__ then when you call  B class using an oject it will print only B constuctor messages
                                           # to access A class init we have to use Super keyword

    def feature3(self):
        print("Feature 3 is working ")

class C(B):  # Multi level inheritance

    def feature4(self):
        print("Feature 4 is working ")

class D():

    def feature5(self):
        print("Feature 5s is working ")

class E(A, D):  # multiple inheritance

        def __init__(self):
            super().__init__()  # here when a E class is sub class of A and B - when you call C class using it's object - it will call only Left hand side of class which is A .
                                # which uses Method resolution Order to pick left side class
            print("Constructor __init__ E")

        def feature6(self):
          print("Feature 6 is working ")


a1 = E()
