def partition(array, start, end):
    pivot = array[start]
    p_1 = start + 1
    p_2 = end

    while p_1 <= p_2:
        if array[p_1] <= pivot:
            p_1 += 1
        if array[p_2] > pivot:
            p_2 -= 1
    
        if p_1 < p_2:
            array[p_1], array[p_2] = array[p_2], array[p_1]
    
    array[start], array[p_2] = array[p_2], array[start]

    return p_2


def q_sort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)

        q_sort(array, start, pivot-1)
        q_sort(array, pivot+1, end)

array = [4, 0, 2, 5, 7, 3, 10]
q_sort(array, 0, len(array)-1)

print(array)
