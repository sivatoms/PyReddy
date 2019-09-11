n = int(input())
k = int(input())

lis = []
for i in range(n):
    lis.append(int(input()))

lis.sort()
print(lis)
sum_lis = []

# ************************************************************************************************************************************
val = 1 - k
answer = 0

sum_lis.append(lis[0])
#print(sum_lis)
for i in range(1, n):
    sum_lis.append(sum_lis[i - 1] + lis[i])
 #   print(sum_lis[i-1],'+', lis[i], '= ', (sum_lis[i - 1] + lis[i]))
print(sum(lis))
print(sum_lis)
for i in range(k):
    answer += val * lis[i]
    print(val, '*', lis[i], ' = ', val*lis[i])
    val += 2
print(answer)

final_answer = answer
for i in range(k, n):
    new_answer = answer + (k - 1) * lis[i] + (k - 1) * lis[i - k] - 2 * (sum_lis[i - 1] - sum_lis[i - k])
    print(answer,'+',(k - 1), '*', lis[i], '+',(k - 1), '*', lis[i - k], '-', 2,'* (',sum_lis[i - 1],'-',sum_lis[i - k],') =  ', (answer + (k - 1) * lis[i] + (k - 1) * lis[i - k] - 2 * (sum_lis[i - 1] - sum_lis[i - k]))     )
    final_answer = min(new_answer, final_answer)
    print(final_answer)
    answer = new_answer


# input

#20
#5
#4504
#1520
#5857
#4094
#4157
#3902
#822
#6643
#2422
#7288
#8245
#9948
#2822
#1784
#7802
#3142
#9739
#5629
#5413
#7232
#print(final_answer)

# input
#7
#3
#10
#100
#300
#200
#1000
#20
#30