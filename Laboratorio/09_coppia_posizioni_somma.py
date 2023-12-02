def findInterval(a, s):
    i = j = 0
    current_sum = a[i]
    while i <= len(a) and j < len(a):
        # current_sum = sum a[i:j+1]
        # sum a[i:j'+1] < sum a[i:j+1] per ogni j' > j
        # sum a[i':j+1] > sum a[i:j+1] per ogni i' < i
        if current_sum == s:
            return i, j
        elif current_sum < s:
            j += 1
            current_sum += a[j] if j < len(a) else 0
        else: # current_sum > s
            i += 1
            current_sum -= a[i-1]
    return -1, -1


a = [int(x) for x in input().split(" ") if x]
s = int(input())
i, j =  findInterval(a, s)
print(i, j)