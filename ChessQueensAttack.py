
# number of ways Queen can attack in a chess board game-- with the given obstacles

n, k = map(int, input().strip().split())

rq, cq = map(int, input().strip().split())

R = n - cq
L = cq - 1
U = rq - 1
B = n - rq
if (rq-1) > (cq-1):
    LU = (cq-1)
else:
    LU = (rq-1)

#LU = 0 #   if U>L ?   L else U

if (n-rq) > (cq-1):
    LB = (cq-1)
else:
    LB = (n-rq)

#print(LB)

#LB = 0 # if B>L ?  L else B
#RU = 0 # if U>R? R else U

if (rq-1) > (n-cq):
    RU = R
else:
    RU = U
#RB = 0 # if B>R? R else B
if (n-rq) > (n-cq):
    RB = n-cq
else:
    RB = n-rq
#print(RB)



if k == 0:
    if rq == cq == n:
        print(3*(n-1))
    else:
        print(L + R + U + B + LU + LB + RU + RB)

else:
    try:
        for i in range(k):
            ob1, ob2 = map(int, input().split())
        #for i in range(k):
         #   ob1, ob2 = map(int, input().strip().split())
            #print(ob1, ob2)
            # LEFT SIDE
            if rq == ob1 and ob2 < cq:
                if L < ((cq-1)-ob2): # 0 < 5 :
                    pass
                else:
                    L = ((cq-1)-ob2)
            #print(L)

            # RIGHT SIDE
            if rq == ob1 and ob2 > cq:
                if R < (n - cq) - abs((n - ob2)+1):  # 5 < (6-5) = 5 < 1 :
                    pass
                else:
                    R = (n - cq) - abs((n - ob2) + 1)
            #print(R)

            # UP SIDE
            if rq > ob1 and ob2 == cq:
                if U < ((rq - 1) - ob1):  # 0 < 5 :
                    pass
                else:
                    U = ((rq - 1) - ob1)
            #print(U)

            # BOTTOM SIDE
            if rq < ob1 and ob2 == cq:
                if B < (n - rq) - abs((n - ob1)+1):  # 5 < (6-5) = 5 < 1 :
                    pass
                else:
                    B = (n - rq) - abs((n - ob1) + 1)
            #print(B)

            # LEFT UP DIAGONAL
            if rq > ob1 and cq > ob2 and (rq - ob1) == (cq - ob2):
                #print(ob1,ob2)
                if rq - ob1 == 1:
                    LU = 0
                    #print('', LU)
                else:
                    if rq>cq:
                        if LU > ((cq-1) - ob2):
                            LU = ((cq-1) - ob2)
                    else:
                        if LU> ((cq - ob2) -1):
                            LU = ((cq - ob2) -1)
            #print(LU)

            # LEFT BOTTOM DIAGONAL
            if rq < ob1 and cq > ob2 and (ob1 - rq) == (cq - ob2):
                if ob1 - rq == 1:
                    LB = 0
                else:
                    if rq < cq:
                        if LB > (ob1 - rq) - 1:
                            LB = (ob1 -rq) -1
                            #print('1st ', LB)
                        else:
                            if LB > ((ob1 - 1) - rq):
                                LB = (ob1 - 1) - rq
                               # print('2nd  ', LB, ob1, rq)
                    else:
                        if LB > ((ob1 - rq)):
                            LB = (ob1 - rq)-1
                            #print('2nd ', ob1, rq, 1)
                    #print(LB)
            #print(LB)

            # RIGHT UP DIAGONAL
            if rq > ob1 and cq < ob2 and (rq - ob1) == (ob2 - cq):
                #print(ob1,ob2)
                if rq - ob1 == 1:
                    RU = 0
                    #print('', LU)
                else:
                    if rq>cq:
                        if RU > ((rq-1) - ob1):
                            RU = ((rq-1) - ob1)
                    else:
                        if RU > ((rq - ob1) - 1):
                            RU = ((rq - ob1) - 1)

            # RIGHT BOTTOM DIAGONAL
            if rq < ob1 and cq < ob2 and (ob1 - rq) == (ob2 - cq):
               # print('0th -----------------------------')
                if ob1 - rq == 1:
                    RB = 0
                else:
                 #   print('1st -----------------------------')
                    if rq < cq:
                  #      print('2rd -----------------------------')
                        if RB > (ob2 - cq) - 1:
                            RB = (ob2 -cq) -1
                   #         print('1st ', LB)
                        else:
                            if RB > (ob2 - 1) - cq:
                                RB = (ob2 - 1) - cq
                    #            print('2nd  ', RB, ob2, cq)
                    else:
                     #   print('3rd -----------------------------')
                        if RB > (ob2 - cq) - 1:
                            RB = (ob2 - cq)-1
                      #      print('4th ', ob2, cq, 1)

        #print('Left side kills: ', L)
        #print('Right side kills: ', R)
        #print('Up side kills: ', U)
        #print('Bottom side kills: ', B)
        #print('Left Diag Up: ', LU)
        #print('Left Diag Bottom: ', LB)
        #print('Right Diag Up: ', RU)
       # print('Right Diag Bottom: ', RB)

        print(L+R+U+B+LU+LB+RU+RB)
    except:
        pass

# input
#5 3
#4 3
#5 5
#4 2
#2 3

# output 10

    #l = (c_q - 1);
    #r = (n - c_q);
    #u = (n - r_q);
    #b = (r_q - 1);
    #lu = u >= l ? l: u;
    #lb = b >= l ? l: b;
    #ru = u >= r ? r: u;
    #3rb = b >= r ? r: b;