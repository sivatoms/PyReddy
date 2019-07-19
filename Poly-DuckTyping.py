

class PyCharm():

    def execute(self):              # execute method
        print("Compiling...")
        print("Running...")

class MyEditor():

    def execute(self):                      # execute method --
        print("Provide more shortcuts")
        print("Enable auto chek")
        print("Compiling")
        print("Running")
class Laptop:

    def code(self, ide):            # here if we have object(ide) which has execute method in it then it does not matter where the method resides in any classes
        ide.execute()


#ide =PyCharm()   # we can chages class to access other class execute methods without changing object name
ide = MyEditor()

lap = Laptop()

lap.code(ide)   # accessing other class method with same name which has in different classes is duckTyping
