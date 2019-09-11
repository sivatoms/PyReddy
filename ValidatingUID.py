
 # validating Unique ID's depending on given rules such as 1 . 2 UPPERCASE CHAR  2.HAVE 3 digits 3.ONLY have a-zA-Z0-9 4.No repeat of char or digit 5. should have 10 char

import re

def validate(uid):
    if len(uid) == 10:
        PH = re.findall(r'[a-zA-Z0-9]', uid)
        TP = set(PH)  # set takes only unique values
        print(TP)
        if len(TP) == 10:
            UP = re.findall(r'[A-Z]', uid)
            NM = re.findall(r'[0-9]', uid)
            if len(UP) >= 2 and len(NM) >= 3:
                 print('Valid')
            else:
               print('Invalid')
        else:
            print('Invalid')
    else:
        print('Invalid')

for i in range(int(input())):
     validate(input())


a = 'B1CD102354'
print(re.findall(r'[a-zA-Z0-9]', a))
#print(re.findall(r'[0-9]', a))