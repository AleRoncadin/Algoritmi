def quickSelect(a, h, i=0, j=None):
    if j is None:
        j = len(a)

    if i >= j:  # Caso base: la sotto-sequenza è vuota
        return None

    k = partition(a, i, j)

    # Numero di elementi nella partizione sinistra incluse il pivot
    nLeft = k - i + 1  

    if h == nLeft - 1:  # Se h è il pivot
        return a[k]
    elif h < nLeft:  # Se h è nella partizione sinistra
        return quickSelect(a, h, i, k)
    else:  # Se h è nella partizione destra
        return quickSelect(a, h - nLeft, k + 1, j)

def partition(a, i, j):
    pivot = a[j - 1]
    k = i
    for h in range(i, j - 1):
        if a[h] < pivot:
            a[k], a[h] = a[h], a[k]
            k += 1
    a[k], a[j - 1] = a[j - 1], a[k]
    return k

a = [int(x) for x in input().split(" ") if x]
h = int(input()) - 1
print(quickSelect(a, h))
