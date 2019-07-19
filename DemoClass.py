
class Computer:

    def __init__(self, cpu, ram):    # it will be called automatically  - it is  constructor
        #print("in init...")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("the Config is : ", self.cpu, self.ram)  # you have to call manually


com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)
com1.config()
com2.config()
