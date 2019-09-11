# re.sub(pattern, replace, string, count=0, flags=0)¶
import re
#ot = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',      r'static PyObject*\npy_\1(void)\n{',       'def myfunc():')
#print(ot)
#patern = re.compile(r'def\s+(\w*)\s*\(\)\:')
#replace = re.compile(r'static PyObject*\npy_\\1(void)\n{')
#text = 'def myfunc():'
#print(re.sub(patern, r'static PyObject*\npy_\1(void)\n{', text))

#print(re.search(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):', text))

#input = 'def myfunc():'
#result = re.sub('def(\w)', r'\1', input)
#print(re.search(r'def\s+(\w)', result))
#print(result)

#temp = 'if a + b > 0 && a - b < 0:'
#temp2 = 'elif a*b > 10 || a/b < 1:'

#print(re.sub(r'\s+([&&])+\s', r' and ', temp))
#res = re.sub(r'\s+([&&])+\s', r' and ', temp)
#if re.match(r'\w*or\s+([||])+\s', temp):
    # print(temp)
#else:
 #   res = re.match(r'\s+([||])+\s', temp)
    #print(res,'seconde')
#print(res)
#print(re.sub(r'\s+([||])+\s', r' or ', temp))



#res = re.search(r'\s+(&&)+\s', temp)
#if re.search(r'\s+(&&)+\s', temp):


# coding challenege

n = int(input())
for i in range(n):
    temp = input()
    result = re.sub(r'(?<= )(&&)(?= )', 'and', re.sub(r'(?<= )(\|\|)(?= )', 'or', temp))  #c here we used re.sub within the re.sub
    print(result)
    #else:
       # print(temp)