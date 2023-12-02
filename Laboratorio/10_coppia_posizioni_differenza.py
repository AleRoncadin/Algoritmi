def findMaxDiff(a):
    # calcola i minimi per prefissi crescenti
    mins = [float('+inf')] * (len(a) + 1)
    argMins = [None] * (len(a) + 1)
    for j in range(len(a)):
        # mins[j] = min a[0,...,j-1]
        if a[j] < mins[j]:
            mins[j + 1] = a[j]
            argMins[j + 1] = j
        else:
            mins[j + 1] = mins[j]
            argMins[j + 1] = argMins[j]
    # calcolo l'escursione massima
    maxDiff = float('-inf')
    argMaxDiff = None
    for j in range(len(a)):
        diff = a[j] - mins[j]
        if diff > maxDiff:
            maxDiff = diff
            argMaxDiff = (argMins[j] , j)
        
    return argMaxDiff


a = [int(x) for x in input().split(" ") if x]
i, j =  findMaxDiff(a)
print(i, j)