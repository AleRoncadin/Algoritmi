from __future__ import print_function

# pip install pygraphviz

def quicksort(a, low, high):
    if high - low <= 1:
        return
    
    middle = partition(a, low, high)
    quicksort(a, low, middle)
    quicksort(a, middle, high)
    

def partition(a, low, high):

    #          low      1  
    # a = ... |<=|<=|<=|>|>|>|X|?|?|p| ...
    p = a[high - 1] # pivot
    i = low

    for j in range(low, high - 1):
        if a[j] <= p:
            # scambio a[i] con a[j] e poi incremento i
            a[i], a[j] = a[j], a[i]
            i += 1

    #          low      i           j = high - 1  
    # a = ... |<=|<=|<=|>|>|>|>|>|>|p| ...
    a[i], a[high - 1] = a[high - 1], a[i]

    #          low      i           j = high - 1  
    # a = ... |<=|<=|<=|p|>|>|>|>|>|>| ...
    return i

def main():
    a = [1,5,3,9,10]
    quicksort(a, 0, len(a))
    print(a)

if __name__ == "__main__":
    main()