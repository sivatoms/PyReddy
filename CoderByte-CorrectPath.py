def CorrectPath(str):
    import random
    st1 = str
    bool = True
    lt = ['r', 'l', 'u', 'd']
    while bool:
        temp = list(st1)
        for _ in range(len(list(q for q in list(st1) if q == '?'))):
            temp[temp.index('?')] = random.choice(lt)
        #print(temp, '*******************************************************')
        if len(temp) == 8 and ('u' not in temp and 'l' not in temp) and sum(1 for i in temp if i == 'd') == 4 and sum(
                1 for i in temp if i == 'r') == 4:
            bool = False

        #elif len(temp) > 8 and ('u' not in temp or 'l' not in temp):
         #   bool = True

        elif len(temp) > 8 and (
                temp[0] == 'u' or temp[0] == 'l' or temp[len(temp) - 1] == 'u' or temp[len(temp) - 1] == 'l'):
            bool = True

        elif len(temp) > 8 and (temp[0] != 'u' or temp[0] != 'l' or temp[len(temp) - 1] != 'u' or temp[len(temp) - 1] != 'l'):
            old = []
            i2, j2 = 1, 1
            for j in temp:

                if j == 'd':
                    i2 += 1
                    #print(temp, '---', old, '--', (i2, j2))
                    if (i2, j2) not in old:
                        old.append((i2, j2))
                        if i2 == 5 and j2 == 5 and len(old) == len(temp):
                            bool = False
                            break
                    else:
                        break

                elif j == 'r':
                    j2 += 1
                    #print(temp, '---', old, '--', (i2, j2))
                    if (i2, j2) not in old:
                        old.append((i2, j2))
                        if i2 == 5 and j2 == 5 and len(old) == len(temp):
                            bool = False
                            break
                    else:
                        break

                elif j == 'u':
                    i2 -= 1
                    #print(temp, '---', old, '--', (i2, j2))
                    if (i2, j2) not in old:
                        old.append((i2, j2))
                        if i2 == 5 and j2 == 5 and len(old) == len(temp):
                            bool = False
                            break
                    else:
                        break

                elif j == 'l':
                    j2 -= 1
                    #print(temp, '---', old, '--', (i2, j2))
                    if (i2, j2) not in old:
                        old.append((i2, j2))
                        if i2 == 5 and j2 == 5 and len(old) == len(temp):
                            bool = False
                            break
                    else:
                        break
                else:
                    break


    return (''.join(i3 for i3 in temp))

# keep this function call here
print(CorrectPath(input()))

# Sample Test Cases
# Input:"???rrurdr?"
#
# Output:dddrrurdrd
#
# Input:"drdr??rrddd?"
#
# Output:drdruurrdddd

# test cases
#  For the input "drdr??rrddd?" your output was incorrect. The correct answer is drdruurrdddd.
# 2. For the input "rd?u??dld?ddrr" your output was incorrect. The correct answer is rdrurrdldlddrr.
# 3. For the input "dddd?uuuurrr????" your output was incorrect. The correct answer is ddddruuuurrrdddd.
# 4. For the input "ddr?rdrrd?dr" your output was incorrect. The correct answer is ddrurdrrdldr.
# 5. For the input "rdrdr??rddd?dr" your output was incorrect. The correct answer is rdrdruurdddldr.

