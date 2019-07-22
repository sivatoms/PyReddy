# re.sub(pattern, repl, string, count=0, flags=0)¶
import re
ot = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',      r'static PyObject*\npy_\1(void)\n{',       'def myfunc():')
#print(ot)
patern = re.compile(r'def\s+\w\(\)\*:')
#replace = re.compile(r'static PyObject*\npy_\1(void)\n{')
text = 'def myfunc():'
print(re.sub(patern, r'static PyObject*\npy_\1(void)\n{', text))

