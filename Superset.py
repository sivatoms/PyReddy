# The issuperset() method returns True if a set has every elements of another set (passed as an argument). If not, it returns False.
# Set A is said to be the superset of set B if all elements of B are in A.

s1 = set(input().split())
b = []
for i in range(int(input())):
    t1 = set(input().split())
    b.append(s1.issuperset(t1))

print(all(b))  # here all command checks if all elements in the list are true or not - else prints-false
