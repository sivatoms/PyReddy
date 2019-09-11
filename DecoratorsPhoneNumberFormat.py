
# formating phone numbers in specified order
# here c[-10:-5] will produce  number of char from right to left of a given string ( - symbol always count the char from right to left)

def wrapper(f):
    def fun(l):
        f("+91 " + c[-10:-5] + " " + c[-5:] for c in l)
        #pat = re.compile(r'(0|91|\+91)?(\d{5})(\d{5})')  # this is using regex
        # give it standard prefix and copy the groups
        #l = [re.sub(pat, r"+91 \2 \3", x) for x in s]    # this is using regex

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


# another exapmle of working with decorators
import operator
# My solution has an error
def person_lister(f):
    def inner(people):
        l = people
        lst = []
        for i in range(len(l)):
            temp = l[i]
            r = []
            r.append(temp[0])
            r.append(temp[1])
            r.append(int(temp[2]))
            r.append(temp[3])
            lst.append(r)
            lst.sort(key=operator.itemgetter(2))
        #res = sorted(people, key=lambda x: int(x[2]))
        #return f(l)
        return map(f, sorted(people, key=lambda x: int(x[2])))  # this is short solution
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

# input
#3
#s h 20 M
#f g 21 F
#t y 15 M