
# Validating Credit Card Numbers with given business logic
# It must start with a 4, 5 or 6.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It may have digits in groups of 4, separated by one hyphen "-".
# It must NOT use any other separator like ' ' , '_', etc.
# It must NOT have 4 or more consecutive repeated digits.

import re

def validate(CD):
    #print(len(CD))
    if (len(CD) == 19 or len(CD) == 16) and (CD[0] == '4' or CD[0] == '5' or CD[0] == '6'):
        #print(re.search(r'1111|2222|3333|4444|5555|6666|7777|8888|9999|0000', CD))
        #print(re.search(r'[0-9]', CD))
        if re.search(r'\-', CD):
            spl = re.split(r'\-', CD)
            #print(spl, len(spl))
            if len(spl[0]) == 4 and len(spl[1]) == 4 and len(spl[2]) == 4 and len(spl[3]) == 4:
                CD = re.sub(r'\-', '', CD)
                #print(CD)
                if len(CD) == 16 and re.match(r'[0-9]', CD) and re.search(r'1111|2222|3333|4444|5555|6666|7777|8888|9999|0000', CD):
                    print('Invalid')
                else:
                    print('Valid')
            else:
                print('Invalid')

        elif re.match(r'[0-9]', CD) and re.search(r'1111|2222|3333|4444|5555|6666|7777|8888|9999|0000', CD):
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')
for i in range(int(input())):
    validate(input())


# 5111116789123456
# 5222216789123456
a = '61230-567-8912-3456'
#print(re.split(r'\-', a))
