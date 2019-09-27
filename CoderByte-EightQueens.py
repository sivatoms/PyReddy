# input
# ["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"]
def EightQueens(strArr):
    import re
    n = 8
    res = list(re.findall(r'[0-9]+', strArr))
    a = []
    for i in range(len(res)-1):
        if (i+1) % 2 != 0:
            a.append((int(res[i]), int(res[i+1])))

    flag = False
    for j in range(n-1):
       for k in range(n-1):
           r = a[j]
           check = a[k+1]
           rq, cq = r[0], r[1]
           ob1, ob2 = check[0], check[1]
           # LEFT
           if rq == ob1 and ob2 < cq:
               flag = True
               #print('--LEFT--')
            # RIGHT SIDE
           elif rq == ob1 and ob2 > cq:
              flag = True
              #print('--RIGHT--')

            # UP SIDE
           elif rq > ob1 and ob2 == cq:
             flag = True
             #print('--UP--')

            # BOTTOM SIDE
           elif rq < ob1 and ob2 == cq:
               flag = True
               #print('--BOTTOM--')
           # LEFT UP DIAGONAL
           elif rq > ob1 and cq > ob2 and (rq - ob1) == (cq - ob2):
               flag = True
               #print('LEFT UP DIAGONAL')
           # LEFT BOTTOM DIAGONAL
           elif rq < ob1 and cq > ob2 and (ob1 - rq) == (cq - ob2):
               flag = True
               #print('LEFT BOTTOM DIAGONAL')
           # RIGHT UP DIAGONAL
           elif rq > ob1 and cq < ob2 and (rq - ob1) == (ob2 - cq):
               flag = True
               #print('RIGHT UP DIAGONAL')
           # RIGHT BOTTOM DIAGONAL
           elif rq < ob1 and cq < ob2 and (ob1 - rq) == (ob2 - cq):
               flag = True
               #print('RIGHT BOTTOM DIAGONAL')

           if flag:
               break
       if flag:
           #print(rq, cq, ob1, ob2)
           strArr = re.sub(' ','',"\""+str(a[j])+"\"")
           break
       else:
           strArr = "true"
    # code goes here
    return strArr


# keep this function call here
print(EightQueens(input()))
