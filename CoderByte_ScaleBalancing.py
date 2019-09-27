
# Challenge
# Have the function ScaleBalancing(strArr) read strArr which will contain two elements, the first being the two positive integer weights on a balance scale (left and right sides) and the second element being
# a list of available weights as positive integers. Your goal is to determine if you can balance the scale by using the least amount of weights from the list, but using at most only 2 weights.
# For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means there is a balance scale with a weight of 5 on the left side and 9 on the right side. It is in fact possible to balance this scale by
# adding a 6 to the left side from the list of weights and adding a 2 to the right side. Both scales will now equal 11 and they are perfectly balanced. Your program should return a comma separated string of
# the weights that were used from the list in ascending order, so for this example your program should return the string 2,6
#
# There will only ever be one unique solution and the list of available weights will not be empty. It is also possible to add two weights to only one side of the scale to balance it.
# If it is not possible to balance the scale then your program should return the string not possible.

# Sample Test Cases
# Input:["[3, 4]", "[1, 2, 7, 7]"]
#
# Output:"1"
#
#
# Input:["[13, 4]", "[1, 2, 3, 6, 14]"]
#
# Output:"3,6"
#
# Input:["[5, 9]", "[1, 2, 6, 7]"]
#
# Output:"2,6"
# i/p  ["[6, 2]", "[1, 10, 6, 5]"]  and o/p   :  1, 5

import re
from itertools import combinations
def ScaleBalancing(StrArr):
    k = re.findall(r'[0-9]+', StrArr)
    l1 = [int(k[0]), int(k[1])]
    l2 = list(int(i) for i in k[2:])

    result = ''
    if l1[0] > l1[1]:
        for x in l2:
            if l1[1] + x == l1[0]:
                result = str(x)
        r1 = []
        if result == '':
            for x in l2:
                for y in l2:
                    if x + l1[0] == y + l1[1]:
                        if (x,y) not in r1:
                            r1.append((x,y))

            if len(r1)>1:
                e = min(r1)
                result = str(e[1])+','+str(e[0])


        if result == '':

            temp = list(combinations(l2, 2))
            for y in temp:
                if sum(y)+l1[1] == l1[0]:
                    result = str(y[0]) +','+str(y[1])

    else:
        for x in l2:
            if l1[0] + x == l1[1]:
                result = str(x)
        r2 = []
        if result == '':
            for x in l2:
                for y in l2:
                    if x + l1[0] == y + l1[1]:
                        if (x, y) not in r2:
                            r2.append((x, y))

            if len(r2) > 1:
                e2 = min(r2)
                result = str(e2[0]) + ',' + str(e2[1])



        if result == '':

            temp = list(combinations(l2, 2))
            for y in temp:
                if sum(y) + l1[0] == l1[1]:
                    result = str(y[0]) + ',' + str(y[1])
    if result == '':
        result = 'not possible'


    return result
print(ScaleBalancing(input()))
