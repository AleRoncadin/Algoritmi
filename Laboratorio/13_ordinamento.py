def quickSort(a, i = 0, j = None):
    if j == None:
        j = len(a)

    if j - 1 <= i:
        return
    
    k = partition(a, i, j)
    quickSort(a, i, k)
    quickSort(a, k + 1, j)

def partition(a, i, j):
    pivot = a[j - 1]
    k = i
    h = i
    while 0 <= k <= h < j:
        if a[h] <= pivot:
            a[k], a[h] = a[h], a[k]
            k += i
        h += i
    return k - 1

a = [int(x) for x in input().split(" ") if x]
quickSort(a)
print(a)
