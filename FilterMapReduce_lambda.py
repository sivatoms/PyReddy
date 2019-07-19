from functools import reduce

## Filter functio can be used to filter data eg : finding even nums from a list
## Map functionn is used to map eg : adding or douling the list
## Reduce Function reduces the whole list into one- and reduce function needs to be imported from a modul called functools

#all these functions takes two parameter as function, values

nums = [2,5,1,7,9,6,0,10]

evens = list(filter(lambda a : a%2== 0,nums))
print(evens)
doubles = list(map(lambda a : a*2,evens))
print(doubles)
sum = reduce(lambda a,b : a + b,doubles)  ## reduce duntions takes two values and a function
print(sum)

