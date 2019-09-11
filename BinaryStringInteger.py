print(4|1)  # here pipe operator works as addition
print(bin(4|1))  # bin converts the added numbers to binary
print(str(bin(4|1)))  # str converts that binary number to string
print(str(bin(4|1))[2:].count('1')) # now we take the only binary part from ( ex :  ob101)  which is 101 and count the number of '1' in the string


# converting string binary number to integer number
s = '001'
print(int(s, 2))