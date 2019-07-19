## There are 3 types of methods - 1. Instance methos, 2.Class Methods, 3.Static Methods

class Student():

    School = "YVU"

    def __init__(self, m1, m2, m3):   # Instance methods can be used with objets
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.School

    @staticmethod
    def info():
        print("This is a YVU College with 200 people ..")

s1 = Student(34, 12, 56)  # for instance methods you have to pass parameters here in the class
s2 = Student(45, 76, 32)

print(s1.m1, s1.m2, s1.m3,"aveg is :", s1.avg())
print(s2.m1, s2.m2, s2.m3, "avg is :", s2.avg())

print(Student.getSchool())   #--Class methods
Student.info()        #--Static Method

