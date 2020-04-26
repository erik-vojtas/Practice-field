# Selection Sort Algorithm

def SelectionSortAlgorithm(array):
    print(f'unsorted array: {array}')
    swaps = 0
    comparisons_count = 0
    for i in range(len(array)):
        print(f'iteration: {i+1}')
        min_position = i
        for j in range(i+1, len(array)):
            comparisons_count += 1
            if array[min_position] > array[j]:
                min_position = j
        if i != min_position:
            array[min_position], array[i] = array[i], array[min_position]
            swaps += 1
        print(array)
    print(f'sorted array: {array}, swaps: {swaps}, comparison_count: {comparisons_count}')
    return array

array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
SelectionSortAlgorithm(array)