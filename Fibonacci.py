

def fib(n):
    a = 0
    b = 1
    for i in range(0,n+1):

        c = a + b # 2 + 3 = 5
        a = b      # a = 3
        b = c      # b = 5
        #print(a,end=" ")

        if a < 100:
            print(a, end=" ")

    print()
    return a


n = int(input("Enter fib series limit  : "))
#print(n)

result = fib(n)
print("The sum of fib series is : ",result)

# 0 1 1 2 3 5 8 13