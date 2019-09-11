# deque is double end que- we can perform adding from left or right, reverse, rotate, pop elements from the list or deque
from collections import deque

d = deque()

for i in range(int(input())):
    l = input().split()
    if len(l) > 1:
        eval('d.{0} ({1})'.format(l[0], int(l[1])))
    else:
        eval('d.{0}()'.format(l[0]))
for r in d:
    print(r, end=' ')


from collections import deque
for _ in range(int(input())):
    _, deq = input(), deque(map(int, input().split()))
    while len(deq) > 1:
        if deq[0] >= deq[1]:
            deq.popleft()
        elif deq[-1] >= deq[-2]:
            deq.pop()
        else:
            print('No')
            break
    else:
        print('Yes')