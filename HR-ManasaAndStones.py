
T = int(input())
for i in range(T):
    n = int(input())
    a = int(input())
    b = int(input())
    #print(' '.join(map(str,sorted({x*a+(n-1-x)*b for x in range(n)}))))


# testing purpose only
for k in range(n):
    print('k : ', k, ' a : ', a, ' n : ', n, ' b : ', b)
    #print(k * a + (n-1-k)*b)
    print('k*a :',k*a, ' n-k-1 :',n-k-1, ' b : ',b,' k*a+(n-k-1)*b =  ',  k*a + (n-k-1) *b)
    print('----------------------------------------------')

# input
# 2 ---test cases
# 3 ---n
# 1 ---a
# 2 ---b

# 4 --- n
# 10 ---a
# 100 ---b

# output
# 2 3 4
# 30 120 210 300