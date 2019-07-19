
# Multithreading means breaking taks into samll tasks..
# The whole code runs using Main Thread..
# We can pause the main thread for our methods using threading

from threading import *
from time import sleep


class Hello(Thread):  # using Thread we can share the task to different core so that the code tasks divided into small tasks
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

#t1.run()
#t2.run()
t1.start()
sleep(0.2)
t2.start()

t1.join() ## Join method is used to add the Main thread to queue because the main thread executes all the statements in the program
t2.join()   # this way Bye statement will print at he end

print("Bye")
