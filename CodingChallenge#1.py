#Write a program which will take list of numbers as input and find all sequences in the lsit which are in ascending order. then find the addition of numbers of each sequence and give largest addition between sequences as output
# input -  [ 4,5,6,2,1,2,3,4,12,6,4,2,1,5,8,9 ]   -- Sequences - [4,5,6] [1,2,3,4,12] [1,5,8,9]  sum of sequences - [15] [22] [23] - Output : 23


list1 = [4, 5, 6, 2, 1, 2, 3, 4, 12, 6, 4, 2, 1, 5, 8, 9]
# list1 = [1, 5, 8, 9,0]
list1.append(0)
res = []
t = []


def SumOfSeq():
    for i in range(len(list1) - 1):
        # print(i,list1[i],list1[i+1])
        if list1[i + 1] > list1[i]:  # 9 > 8 ?
            if len(res) == 0:
                res.append(list1[i])
                # print(res)
            else:
                # print(i)
                res.append(list1[i])
                # res.append(list1[i+1])
                # print(res)

        else:
            res.append(list1[i])
            # print("Condition failed : ",res)
            break
    d = len(res)
    del list1[:d]

    # print("The Main list  : ",list1)
    # print("The result list : ",res)

    def sumofl():
        if len(res) > 1:

            r = 0
            for i in res:
                r = r + i

            t.append(r)
            print("Sum of Sequence of : ", res, "is : ", r)

    sumofl()


i = len(list1) + 1
while i >= 0:
    SumOfSeq()
    # print(res)
    res1 = res
    res = []
    i -= 1
print("The largest of sum of sequences are : ", max(t))



