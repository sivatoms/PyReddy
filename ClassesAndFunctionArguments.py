
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

# if the function argument stream is None then we need to override and pass EvenStream() as default argument otherwise it will use the passed argument along with the integer n
# here in this task we are calling two different classes depending on the user input such as\
# 2   # means two line of string
# odd 3  # first string 3 odd numbers from 0
# even 2 # second string 2 even numbers from 0

def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
