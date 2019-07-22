
## Search pattern
## search can be don in two way one is with compile pattern other is direct pattern

import re

text = input()
statement = input()


patn = re.compile(statement)
match = re.search(patn, text)


if not match:
    print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end()-1))
    match = patn.search(text, match.start()+1)

