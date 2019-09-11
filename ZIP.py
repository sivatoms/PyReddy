# Zip returns a list of tuples The i-th tuple contains the i-th element of each argument sequence or iterables. if the argument sequences are unequal length then the returned list is truncated to the length of the shortes argument sequence

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print(X)
Z = zip(*X)
print(next(Z))



# Example
N, X = list(map(int, input().split()))  # N students and X scores

l = []
for _ in range(X):
    l.append(list(map(float, input().split()[:N]))) # scores

T = zip(*l)
for i in T:
    #print(i)
    print(sum(j for j in i)/X)  # prints average scores of each students

## input
#5 3
#89 90 78 93 80
#90 91 85 88 86
#91 92 83 89 90.5