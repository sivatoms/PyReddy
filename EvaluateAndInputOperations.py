


#print('{0} {1}'.format('one', 'two'))
#print('one', 'two')

#data = {'first': 'Hodor', 'last': 'Hodor!'}     # Place holder   " : "
#print('{first} {last}'.format(**data))

#s = set()
#result = set()
#n = int(input())
#funname = input()
#for i in range(n):
#eval('s.{0} ({1})'.format(funname, map(int, input().split())))
#    eval('s.{0} ({1})'.format(funname, int(input())))
#print(s)

lst = []
n = int(input())

for k in range(n):
    oper = []
    i = 0
    oper = list(input().split())
    if oper[i] == 'insert':
        lst.insert(int(oper[i+1]), int(oper[i+2]))
    elif oper[i] == 'remove':
        lst.remove(int(oper[i+1]))
    elif oper[i] == 'append':
        lst.append(int(oper[i+1]))
    elif oper[i] == 'sort':
        lst = sorted(lst)
    elif oper[i] == 'pop':
        lst.pop()
    elif oper[i] == 'reverse':
        lst.reverse()
    elif oper[i] == 'print':
        print(lst)
    #eval('lst.{}({}', '{})'.format(oper[i], oper[i+1], oper[i+2]))
    #if oper == 'print':
     #   print(lst)
    #print(oper[i], oper[i+1], oper[i+2])
print(lst)

