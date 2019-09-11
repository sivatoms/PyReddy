import re

s = input()
s
vw = 'aeiou'
kev=0
st =0
for i in range(len(s)):
    if s[i].lower() in vw:
        kev += (len(s) - i)
    else:
        st += (len(s)-i)

if kev > st:
    print("Kevin", kev)
elif kev < st:
    print("Stuart", st)
else:
    print('Draw')
