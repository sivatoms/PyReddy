import re
##  Metacharacters - []  .  ^  $  *  +  {}  ()   \  |

# []   specifies set of characters you wish to match. from the start of the string
a = 'gfdfgdrfg'
print('[] match found ', re.match('[a-z]', a))

#  . period matches any single character except new line (\n)
a = 'ghi'
print('. match is ', re.match('..', a))

# ^ caret is used to check if a string  starts with a certain character.
a = 'shiva'
print('^ match is ', re.match(r'^shi', a))

# $ is used to check if a string ends with a certain character
a = 'shiva'
print('$ match is ', re.search(r'a$', a))

# * matches zero or more occurences of the pattern left to it
a = 'aashiva'
print('* match is ', re.search(r'iv*a', a))

# + matches one or more occurrences of the pattern left to it
a = 'shiiiiva'
print('+ match is ', re.search('sh+i', a))

# ? matches zero or one occurrence of the pattern left to it
a = 'batman-car'
print('? match is ', re.search('ma?n', a))

# {} braces {m,n} means at least m, and at most n repetitions of the pattern left to it
a = 'shivaa123'
print('{} match is ', re.search('a{1,2}', a))
print('{} match is ', re.search('[0-9]{2,3}', a))

# | is used for alternation (or operator)
a = 'shiva'
print('| match is ', re.search('a|v', a))

# () is used to group sub-patterns. eg: (a|b|c)xy match any string that matches either a or b or c followed by xy
a = 'shiva'
print('() match is ', re.search('(h|i)va', a))

# \ is used to escape various characters including all metacharacters. eg: \$a match if a string contains $ followed by a.
a = 'shiva$reddy'
print('\\ match is ', re.search('\$reddy', a))   # \\ is used print \  and \ will wipe out the special meaning of metacharacters

# \A is used to match if the specified characters are at the start of a string
a = 'the mountain view'
print('\A match is ', re.search('\Athe', a))

# \b matches if the specified characters are at the beginning or end of a word
a = 'a loopover'
b = 'the factorial has loo'
print('\\b match is', re.search(r'\bloo', a))  # beginning of a word
print('\\b match is', re.search(r'loo\b', b))  # end of a word

# \B is opposite of \b - and \B matches if specified characters are not at the beginning or end of a word
a = 'a loops for iterations'
b = 'the infinite iterations uses loo'
print('\B match is ', re.search('\Bloo', a))  # beginning of a word is none here
print('\B match is ', re.search('loo\B', b))  # end of a word here is none

# \d matches any decimal digit [0-9]
a = '@shiva1991'
print('\d match is ', re.search('\d', a))  # decimal digit
print('\D match is ', re.match('\D', a))    # Non=Decimal digits or letters

# \s matches where a string contains any whitespace character
a = 'the python'
print('\s match is', re.search('\s', a))





