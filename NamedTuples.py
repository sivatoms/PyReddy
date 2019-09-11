from collections import namedtuple

N = int(input())
t = 0
Cols = input()  #   ID MARKS NAME CLASS
C = Cols.split()

Std = namedtuple('Std', Cols)
for _ in range(N):
    res = Std._make(input().split()).MARKS  # Here _make will pull the value of marks whereas the namedtuples can be shuffled while taking inputs  and the inputs to namedtuples depends on the columns names
    t += int(res)
print(t/N)

# input
#2
#ID MARKS NAME CLASS
#2 20 siva 4
#4 50 red 3