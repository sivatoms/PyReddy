
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
list1 = [x,y,z]
lst = []
def lexico(x,y,z):

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k)!= n:
                    lst.append(i)
                    lst.append(j)
                    lst.append(k)
    return lst

list1 = [x,y,z]
res = lexico(x,y,z)
chunks = [res[x:x+3] for x in range(0, len(res), 3)]   #c this will split the list into sub list
print(chunks)

# Another example

def lexico(s):

    for i in range(len(s)-1)[::-1]:
        if s[i] < s[i+1]:
            for j in range(i+1,len(s))[::-1]:
                print(s[i], s[j])
                if s[i] < s[j]:
                    lis = list(s)
                    lis[i],lis[j]=lis[j],lis[i]
                    return "".join(lis[:i+1]+lis[i+1:][::-1])
    return 'no answer'

for _ in range(int(input())):
    s = input()
    res = lexico(s)
    print(res)

# 6
# lmno
# dcba
# dcbb
# abdc
# abcd
# fedcbabcd

# output
# lmon
# no answer
# no answer
# acbd
# abdc
# fedcbabdc