
# To perform binary search - we need to sort the list first:

pos = -1

def search(lst, n):
    l = 0
    u = len(lst)-1

    for l in range(u+1):
        mid = (l+u)//2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False


n = 702
lst = [4, 7, 8, 12, 45, 99, 102, 702]

if search(lst, n):
    print("Found at : ", pos+1)
else:
    print("Not found")