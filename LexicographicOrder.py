
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
list1 = [x,y,z]
lst = []
def lexico(x,y,z):
    t = []
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