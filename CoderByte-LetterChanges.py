def LetterChanges(str):
    import re
    l = []
    s = list(re.sub('"','',str.lower()))
    vow = ['a', 'e', 'i', 'o', 'u']
    #print(s)
    for one in range(97, 123):
        l.append(chr(one))
    #print(l)
    for i in range(len(s)):
        for j in range(len(l)-1):
          if j <= len(l):
            if l[j] == s[i] and s[i] != ' ':
                #print(l[j+1], s[i])
                s[i] = l[j+1]
                if s[i] in vow:
                    s[i] = s[i].upper()
                    break
                break

    str = ''.join(tt for tt in s)
    # code goes here
    return str


# keep this function call here
print(LetterChanges(input()))
