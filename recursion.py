
# the function calls itself called recursion
# By default pyhton only let you to go until 1000 time recursion
# to customize recursion use sys package

import sys

sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i = i +1
    print("hello",i)
    greet()

greet()