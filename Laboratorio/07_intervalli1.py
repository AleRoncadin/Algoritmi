from __future__ import print_function

try: input = raw_input
except NameError: pass

class SegmentNode:
    low = None
    high = None
    massimo = None
    left = None
    right = None

    def __init__(self, a, low, high):
        assert high - low > 0
        self.low = low
        self.high = high
        if high - low <= 0:
            self.massimo = a[low]
            self.left = None
            self.right = None
        else:
            mid = (low + high) // 2
            self.left = SegmentNode(a, low, mid)
            self.right = SegmentNode(a, mid, high)
            self.massimo = max(self.left.massimo, self.right.massimo)
    


def input_array():
    return [int(x) for x in input().split(" ") if x]

def aux_sum(a):
    # a   =   |1|2|3|4| | | | 
    # aux = |0|1|3|6|10| | | |
    aux = [0] + (len(a) + 1)
    for i in range(0, len(a)):
        aux[i + 1] = aux[i] + a[i]

    return aux

def range_sum_fast(a, i , j, aux):
    return aux[j + 1] - aux[i]

def range_sum(a, i ,j):
    s = 0
    for k in range(i, j + 1):
        s = s + a[k]
    return s

a = input_array()
b = input_array()
c = [(i, j) for (i, j) in zip(b[0::2], b[1::2])]

aux = aux_sum(a)

for (i, j) in c:
    print(range_sum(a, i , j), end = ' ')

# print(a)
# print(c)
