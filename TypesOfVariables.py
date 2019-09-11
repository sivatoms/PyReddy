
# We have two types of variables - 1. Instance variables,  2. Class variables and instance or static variables are same

class Car():

    wheels = 4   # this is a class variable
    def __init__(self):
        self.mil = 10           # These are instance variable - can be changed using objects
        self.com = "BMW"        # These are instance variables

c1 = Car()
c2 = Car()
c1.mil = 12

Car.wheels = 5   # if you use class to chages class variable- they changes for all objects

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)