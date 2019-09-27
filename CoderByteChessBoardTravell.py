# Challenge
# Have the function ChessboardTraveling(str) read str which will be a string consisting of the location of a space on a standard 8x8 chess board with no pieces on the board along with another space on the chess board. The structure of str will be the following: "(x y)(a b)" where (x y) represents the position you are currently on with x and y ranging from 1 to 8 and (a b) represents some other space on the chess board with a and b also ranging from 1 to 8 where a > x and b > y. Your program should determine how many ways there are of traveling from (x y) on the board to (a b) moving only up and to the right. For example: if str is (1 1)(2 2) then your program should output 2 because there are only two possible ways to travel from space (1 1) on a chessboard to space (2 2) while making only moves up and to the right.

def ChessB(pos):
    import re
    t = re.findall(r'[0-9]+', pos)
    l = []
    l2 = []
    for i in range(len(t)):
        l.append(t[i])
        if len(l) == 2:
            l2.append((int(l[0]), int(l[1])))
            l = []
    r1, c1, r2, c2 = (l2[0])[0], (l2[0])[1], (l2[1])[0], (l2[1])[1]
    #print(r1, c1, r2, c2)
    #for i in range(1,r2+1):
     #   for j in range(1,c2+1):
            #print(i,j)

      #      pass

    #print(c2*(c2-c1))
    pos = str(c2*(c2-c1))

    return pos
print(ChessB(input()))

# someone solution
import math


def ChessboardTraveling(instr):

    numup = int(instr[7]) - int(instr[2])
    numright = int(instr[9]) - int(instr[4])
    first = numup + numright
    second = min(numup, numright)
    print(first, second)

    # code goes here
    return int(math.factorial(first) / (math.factorial(second) * math.factorial(first - second)))

# keep this function call here
print(ChessboardTraveling(input()))

# Input:"(1 1)(3 3)"
#
# Output:6
#
#
# Input:"(2 2)(4 3)"
#
# Output:3