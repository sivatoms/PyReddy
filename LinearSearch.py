
pos = -1
def search(lst, n):
    for i in range(len(lst)-1):
        if lst[i] == n:
            globals()['pos'] = i
            return True
    return False

n = int(input())
lst = list(map(int, input().split()))

if search(lst, n):
    print("Found at : ", pos+1)
else:
    print("Not Found ")

