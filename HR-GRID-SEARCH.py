
t = int(input())

for _ in range(t):

    R, C = map(int, input().strip().split())
    g = []
    p = []
    for _ in range(R):
        g.append(list(input().strip()))
    r, c = map(int, input().strip().split())
    for _ in range(r):
        p.append(list(input().strip()))
    cnt = 0
    mt = False
    try:

        for i in range(R-1):
            #print('row is : ', i)
            for j in range(C-1):
                if g[i][j] == p[0][0]:
                    r1, c1 = i+(r), j+(c)
                    if c1<=C:

                        #print(r1, c1, i, j)
                        r2 = 0
                        for ii in range(i,r1,1):
                            c2 = 0

                            for jj in range(j, c1, 1):
                                #print(g[ii][jj], ' position is at : (', ii, jj, ') ', end=' ')


                                if g[ii][jj] == p[r2][c2]:
                                    #print('p at (', r2, c2, ') value is : ', p[r2][c2],  ' g at (', ii, jj, ') value is : ', g[ii][jj])
                                    cnt += 1
                                else:
                                    cnt = 0
                                c2 += 1
                            #print('cnt is : ', cnt)
                            if cnt == r*c:
                                #print('cnt is : ', cnt)
                                mt = True
                                cnt = 0
                                break
                            #print()
                            #print('p is : ', r2, c2, 'g ii, jj is ', ii, jj)
                            r2 += 1


                        if mt:
                            break

                    cnt = 0
                    if mt:
                        break
            if mt:
                break

    except IndexError as e:
        #print(e)
        pass


    if mt:
        print('YES')
    else:
        print('NO')

''''
 input
4 6
123412
561212
123634
781288
2 2
12
34

# output
# YES

# input
1
2 6
999999
121211
2 2
99
11

# output
# YES

'''

