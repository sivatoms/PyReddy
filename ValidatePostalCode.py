import re

a = r"^[1-9][\d]{5}$"   #  Here the digits should satrt with 1-9 and end with 1-9 . including the the number of digits should not exceed 5 means (6 in high level )
b = r"(\d)[?=.\1]"  # (\d)(?=.\1)       #  (\d) give all decimal digits, ?=. will look ahead and \1 is group search

#regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
#regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"	# Do not delete 'r'.

import re
P = input()


print(re.findall(b, P))
#print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

pattern = r"Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")