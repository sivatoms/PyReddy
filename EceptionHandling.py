
# Exception Handling comes into picture when there is an error in the code
# There are 3 types errors we get- 1. CompileTime Error (Syntax errors) 2.Logical error (eg: division error) 3.Runtime error(eg: conection broke or file gets deleted


a = 5
b = 2

try:
    print("Division started;")
    print(a/b)
except ZeroDivisionError as e:
    print("Hey: you cannot divide a numbe rwith zero: ", e)

except ValueError as e:
    print("You have entered invalid data:")

finally:                # Finally can be used to close connection or db or file wehter there is an error or not.
    print("Task completed")