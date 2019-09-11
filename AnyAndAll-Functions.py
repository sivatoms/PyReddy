def test():

    pl = [2, 3, 5, 7, 11]
    N = int(input())
    il = input().split()[:N]
    r = []
    bool = False
    for i in il:
        if int(i)>0:
            r.append(int(i))
    if any([j == j[::-1] for j in il]):  # checks if the list is palindrome or not
       bool = True

    if len(r) == len(il) and bool == True:
        print(True)
    else:
        print(False)


test()

# short solution
#N,n = int(input()),input().split()
#print(all([int(i)> 0 for i in n]), any([j == j[::-1] for j in n]))


