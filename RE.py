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

# ?<= will look behind and ?=  will look ahead
temp = input()
result = re.sub(r'(?<= )(&&)(?= )', ' and ', temp)
print(result)
# {} braces {m,n} means at least m, and at most n repetitions of the pattern left to it
a = 'shivaaaaa123'
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

# \S matches where a string contains any non-whitespace characters
a = 'the python'
print('\S match is ', re.search('\S', a))

# \w matches any alphanumeric character (digits and alphabets) - equal to [a-zA-Z0-9_] and _ (underscore) is also considered as alphanumeric character
a = 'abcdef12_*'
print('\w match is ', re.search('\w', a))

# \W matches any non-alphanumeric character. equal to [^a-zA-Z0-9_]
a = 'shiva @reddy'
print('\W match is ', re.search('\W', a))


# re.findall()   method returns a list of strings containing all matches
a = 'shiva1991day23month07'
print(re.findall('\d', a))
re.findall('([A-Za-z]+) \w+ \d+ \w', "Ja has 6 dogs ra has 7 cats")  # here final all only pulls the names as if it has any groups in the re like () will printout the subsections the othe set of re
# outputs - ja ra
# re.split() method splits the string where there is a match and returns a list of strings where split have occurred
a = 'shiva:1 reddy:2 junna:3.'
print(re.split(r'\d+', a))
print(re.split('\d+', a, 1))  # here 1 is maxsplit - by default maxsplit is zero

# Example split()

regex_pattern = r"[,.]+"	# Do not delete 'r'.   here if [,.]+ these occur in between digits then the split will omit that matched  ,. then print the rest line by line

import re
print("\n".join(re.split(regex_pattern, input()))) #
# input
# 100,000,000.000

# re.sub(pattern, replace, string)    - this method returns a string where matched occurences are replaced with the contect of replace vairable
a = 'abc 12\
dec23  reddy \n 567junna 91'
print(re.sub('\s+', '', a))  # here it replaced everything including multiline and made it into single line of string

# re.subn() method returns the number os replace or substitutions happened
print(re.subn('\s+', '', a))

# () i can be used in the pattern to capture and search that using \1 .. \n in the replace
a = 'def myfunc():'
print(re.sub(r'def\s+(\w*)\s*\(\)\:', r'class project1:\npy_\1(void)\n{',a))

# flags
# . usually stops at new line . to include new line we use flags as 3rd parameter
string = 'sdkjdfd dflnjdfldfnds sdffldfldfl' \
         'ndslnfdsdldsvldsvldldvlndsl'
re.search('.+', string, flags = re.DOTALL)  # here flags = re.DOTALL will include new lines of string to print

# ?P<Name>
re.search(r'\? P<Name>[\w]+', string)
# *********** EXAMPLES *************
# 1.
import re
import email.utils


# input


# dheeraj <dheeraj-234@gmail.com>
# crap <itsallcrap>
# harsh <harsh_1234@rediff.in>
# kumal <kunal_shin@iop.az>
# mattp <matt23@@india.in>
# harsh <.harsh_1234@rediff.in>
# harsh <-harsh_1234@rediff.in>

n = int(input())
lst2= []
for i in range(n):
    r = input()

    #p = re.search(r'([\w*\s+\<\w*\.-_]+)@+(\.)+[a-zA-Z]', r)
    #print(p)
    if re.search(r'([\w\.-_]+)@([a-zA-Z]+).^[a-zA-Z]', r):
        pass
    #elif re.search(r'([\w\.-_]+)@([a-zA-Z]+).{1,3}[?...)]', r):
    #elif re.search(r'([\w\.-_]+)@([a-zA-Z]+)\.+[a-zA-Z]]', r):
    elif re.search(r'<[a-zA-Z](\w|-|\.|_)+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', r):
        ot = re.search(r'<[a-zA-Z](\w|-|\.|_)+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', r)
        lst = list(ot.groups())

        lst2.append(lst)
        print(lst)
        if len(lst2[0])>3:
            pass
        else:
            print(r)
    else:
        pass


# ******** Finding substring in a string and the count of substrings in it.
import re

a = 'ABCDCDC'
s = 'CDC'
l1 = list(a)
r = 0

p = re.compile(r'('+s+')+')

for i in range(len(a)):
    if len(a)>=len(s):
        #k = re.search(r'(CDC)+', a)
        k = re.search(p, a)
        if re.search(p, a):
            l = list(k.span())
            del l1[l[0]]
            a = ''.join(l1)
            r += 1
print(r)

import re
#**** To find a float point number using re
N = int(input())
for _ in range(N):
    try:
        if re.search(r'^[+-]?[\d]*\.[0-9]+$', input()):  # re is magic
            print(True)
        else:
            print(False)
    except:
        pass




