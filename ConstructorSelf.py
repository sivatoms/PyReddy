
class Computer2:

    def __init__(self):
        self.name = "Shiva"
        self.age = 28

    def update(self):
        self.age = 28

    def compare(self, c2):

        if c1.age == c2.age:
            return True 
        else:
            return False



c1 = Computer2()   #---> this is constructor  it calls __init__ methods and it decides memory of objects
c2 = Computer2()


print(c1.name, c1.age)

if c1.compare(c2):
    print("they are same..")
else:
    print("They are different..")

c1.update()

print(c1.name, c1.age)