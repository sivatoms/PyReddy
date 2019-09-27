
# 1. For the input "+d+" your output was incorrect. The correct answer is true.
# 2. For the input "+z+z+z+" your output was incorrect. The correct answer is true.
# 3. For the input "2+a+a+" your output was incorrect. The correct answer is true.
# 4. For the input "+a++" your output was incorrect. The correct answer is true.
# 5. For the input "+z+z+==+a+" your output was incorrect. The correct answer is true.

def SimpleSymbols(str):
    import re
    k = list(str)
    flag = False
    for i in range(1,len(k)-1):
        if re.search(r'[a-z]+', k[i]):
            print(k[i])
            if k[i-1] == '+' and k[i+1] == '+':
                print(k[i-1],k[i], k[i+1])
                flag = True
            else:
                flag = False
                break

        else:

            pass

    if flag:
        if re.search(r'[a-z]+',k[len(k)-1]):
            str = 'false'
        else:
            str = 'true'
    else:
        str = 'false'


    return str


# keep this function call here
print(SimpleSymbols(input()))