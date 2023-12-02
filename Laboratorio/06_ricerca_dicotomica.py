from __future__ import print_function

try: input = raw_input
except NameError: pass

def binary_search(a, low, high, key):
    if high - low <= 1:
        return None
    m = (low + high) // 2
    if a[m] == key:
        return m
    elif key < a[m]:
        return binary_search(a, low, m, key)
    else:
        return binary_search(a, m + 1, high, key)

a = [int(x) for x in input().split(" ") if x]
key = int(input())

print(binary_search(a, 0, len(a), key))