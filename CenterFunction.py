
import string
# Center function adds padding to the specified length in the code
# 1. Sytax -- >    center(length, fillchar)
string1  = 'Shiva Reddy Junna'
cs = string1.center(30,'-')  # here the length of the whole string will be 30 and if the provided string length is less than the specified center length then you will be able to see that in output
print(cs)

cs = string1.center(30) # here we did not give any fill char like above example. so that it will automatically print space
print(cs)  #
n = 5
s2 = '-'.join(string.ascii_lowercase[:n])
print(s2)
l = []
l.append((s2[::-1]+s2[1:]).center(10*n-3, '-'))   # here center function adds extract - to the string and appending it to the list
print(l)

