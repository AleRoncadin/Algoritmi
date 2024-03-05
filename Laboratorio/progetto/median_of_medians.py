def median_of_medians(arr, left, right, k):
    if left == right:
        return arr[left]

    num_elements = right - left + 1
    medians = []

    for i in range(0, num_elements // 5):
        sub_list = sorted(arr[left + i*5 : left + (i+1)*5])
        medians.append(sub_list[2])

    if num_elements % 5:
        sub_list = sorted(arr[left + (num_elements // 5)*5 : right + 1])
        medians.append(sub_list[len(sub_list) // 2])

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = median_of_medians(medians, 0, len(medians) - 1, len(medians) // 2)

    partition_index = partition(arr, left, right, pivot)

    if k == partition_index:
        return arr[k]
    elif k < partition_index:
        return median_of_medians(arr, left, partition_index - 1, k)
    else:
        return median_of_medians(arr, partition_index + 1, right, k)

def partition(arr, left, right, pivot):
    pivot_index = arr.index(pivot)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[right] = arr[right], arr[store_index]
    return store_index

def find_kth_smallest(arr, k):
    # Adatta k per l'indice basato su 0 interno all'algoritmo
    return median_of_medians(arr, 0, len(arr) - 1, k-1)

a = [int(x) for x in input().split(" ") if x]
k = int(input())
print(find_kth_smallest(a,k))
