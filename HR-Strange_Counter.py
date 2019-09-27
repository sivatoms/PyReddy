import time
s_t = time.time()
#print(pow(10, 12), 22 + 24)
def ft(t):
    rem = 3
    while t > rem:
        t = t - rem
        rem *= 2
    return rem - t + 1
t = int(input())
result = ft(t)
print(result)

e_t = time.time()
t_t = e_t - s_t
print('Time is : ', t_t)
# input
# 17
# output
# 5