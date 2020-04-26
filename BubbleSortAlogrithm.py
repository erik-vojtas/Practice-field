#Bubble sort algorithm

def BubbleSortAlgorithm(array):
    print(f'unsorted array: {array}')
    swaps = 0
    comparison_count = 0
    for i in range(len(array)-1):
        print(f'iteration: {i+1}')
        for j in range(len(array)-1-i):
            comparison_count += 1
            if array[j] > array[j+1]:
                helper = array[j]
                array[j] = array[j+1]
                array[j+1] = helper
                swaps += 1
        print(array)
    print(f'sorted array: {array}, swaps: {swaps}, comparison_count: {comparison_count}')
    return array

array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
BubbleSortAlgorithm(array)
