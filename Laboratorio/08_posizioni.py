from __future__ import print_function

try: input = raw_input
except NameError: pass

def input_array():
    return [int(x) for x in input().split(" ") if x]

a = input_array()
s = int(input())

for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == s:
            print(i, j)
            exit()