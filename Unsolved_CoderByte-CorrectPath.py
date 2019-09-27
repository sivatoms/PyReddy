from itertools import permutations
import random

# Challenge
# Have the function CorrectPath(str) read the str parameter being passed, which will represent the movements made in a 5x5 grid of cells starting from the top left position. The characters in the input string will be
# entirely composed of: r, l, u, d, ?. Each of the characters stand for the direction to tatemp[k]e within the grid, for example: r = right, l = left, u = up, d = down. Your goal is to determine what characters the question
# martemp[k]s should be in order for a path to be created to go from the top left of the grid all the way to the bottom right without touching previously travelled on cells in the grid.
#
# For example: if str is "r?d?drdd" then your program should output the final correct string that will allow a path to be formed from the top left of a 5x5 grid to the bottom right.
# For this input, your program should therefore return the string rrdrdrdd. There will only ever be one correct path and there will always be at least one question martemp[k] within the input string.
# Sample Test Cases
# Input:"???rrurdr?"
#
# Output:dddrrurdrd
#
# Input:"drdr??rrddd?"
#
# Output:drdruurrdddd

def CorrectPath(instr):
    st1 = instr
    bool = True
    lt = ['r', 'l', 'u', 'd']
    while bool:
        temp = list(st1)
        for i in range(len(list(q for q in list(st1) if q == '?'))):
            temp[temp.index('?')] = random.choice(lt)
        #print('changed--->', temp)

        if len(temp) == 8 and ('u' not in temp and 'l' not in temp) and sum(1 for i in temp if i == 'd') == 4 and sum(1 for i in temp if i == 'r') == 4:
            bool = False

        elif len(temp) > 8 and ('u' not in temp or 'l' not in temp):
            bool = True
        elif len(temp) > 8 and (temp[0] == 'u' or temp[0] == 'l' or temp[len(temp)-1] == 'u' or temp[len(temp)-1] == 'l'):
            bool = True
        elif len(temp) > 8 and (temp[0] != 'u' or temp[0] != 'l' or temp[len(temp)-1] != 'u' or temp[len(temp)-1] != 'l'):
            flag = True
            i2, j2 = 1, 1
            while flag:
                t = ''
                for j in range(len(temp)):
                    if temp[j] == 'd' and i2 < 5:
                        if i2 >= 1 and t == 'u':
                            flag = False
                            break
                        else:
                            i2 += 1
                            t = temp[j]
                    elif temp[j] == 'r' and j2 < 5:
                        if j2 >= 1  and t == 'l':
                            flag = False
                            break
                        else:
                            j2 += 1
                            t = temp[j]
                    elif temp[j] == 'u':
                        if i2 >= 1 and i2 < 5 and i2 - 1 != 1 and t == 'd' and temp[j+1] == 'l':
                            flag = False
                            break
                        else:
                            i2 -= 1
                            t = temp[j]
                    elif temp[j] == 'l':
                        if j2 >= 1 and j2 < 5 and j2 - 1 != 1 and t == 'r':
                            flag = False
                            break
                        else:
                            j2 -= 1
                            t = temp[j]

                    elif i2 == 5 and j2 == 5:
                        bool = False
                        print(temp)
                        print(i2, j2, t, j)
                        break
                    else:
                        #print(temp)
                        print('failed : ', i2, j2, ', prev-: ', t, ' current : ',temp[j], ', pos :', j)
                        flag = False
                        break
        else:
            bool = False



    return (''.join(i3 for i3 in temp))
# temp[k]eep this function call here
print(CorrectPath(input()))



