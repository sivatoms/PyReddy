
# Operator Overloading will allow us to define user methods which can override the operator methods such as __add__ , __sub__

class Student():

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):

        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):

        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {} '.format(self.m1, self.m2)

s1 = Student(58, 69)
s2 = Student(69, 65)
print(58+69, 69+65)
print(s1+s2)

if s1 > s2:
    print("S1 WINS")
else:
    print("S2 WINS")

print(s2)



