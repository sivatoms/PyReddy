
# inner class is a inside of a class

class Student():

    School = "YVU"

    def __init__(self):
        self.name = "Shiva"
        self.rollno = 2
        self.lap = self.Laptop()  # creating an object for inner class on outer class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop():

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram  = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student()
s2 = Student()

#s1 = Student.Laptop()  # this is another way of creating an object for inner class outside of al the classes
s1.show()
