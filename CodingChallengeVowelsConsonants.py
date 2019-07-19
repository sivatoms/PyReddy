import re

string = input()
con = re.findall(r'\w', 'qwrtypsdfghjklzxcvbnm')  # consonants

vow = ['a', 'e', 'i', 'o', 'u']  # vowels
lst = re.findall(r'\w', string)
res = ''
counter = 0
l = 0
n = 0
#print(lst[2].lower())
for i in range(len(lst)):
    t = lst[i].lower()
    if t == 'a' or t == 'e' or  t == 'i' or t == 'o' or t == 'u':
        if counter == 1:
            l += 1
            res = res + lst[i]
    else:                                       # this condition checks for vowels should be between consonants
        #print(lst[i],'Not equal')
        counter = 1
        if l>=2 and len(res)>=2:                # this condition checks 2 or more vowels one after another in a string
            #print(res,'equal',l)
            print(res)
            n = n+1
        res = ''
if n == 0:
    print(-1)


# rabcdeefgyYhFjkIoomnpOeorteeeeet
# abaacaadaakaalaas
# match a single character not present in the list below


# this is the short solution using regular expressions
import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))