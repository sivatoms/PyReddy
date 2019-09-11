from functools import reduce
cube = lambda x: pow(x,3)# complete the lambda function

def fibonacci(n):
    a = 0
    b = 1
    l = []
    l.append(0)
    for i in range(n-1):

        c = a + b  # 2 + 3 = 5
        a = b  # a = 3
        b = c  # b = 5
        # print(a,end=" ")

        if a < 100:
            #print(a, end=" ")
            l.append(a)

    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    #fibonacci(n)


