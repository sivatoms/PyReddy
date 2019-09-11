import re


# collections.counter() can be used to count the number of occurences of each char in a given string
# This will search for first consecutive string or repeating string in the given string   here \1 means first group of first 99 groups
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
