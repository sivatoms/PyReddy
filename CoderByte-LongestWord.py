
#"123456789 98765432"

def LongestWord(sen):
    import re
    l = re.findall(r'[a-z0-9]+', str(sen))
    print(l)
    k = ''
    res = 0
    for i in l:
        if len(i) > res:
            res = len(i)
            k = i
    print(k)
    sen = str(k)

    # code goes here
    return sen


# keep this function call here
print(LongestWord(input()))