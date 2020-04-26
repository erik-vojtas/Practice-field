#Insertion Sort Algorithm

def InsertionSortAlgorithm(array):
    print(f'unsorted array: {array}')
    for i in range(1, len(array)):
        store = array[i]
        j = i - 1
        while j >= 0 and store < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = store
        print(f'{i}. iteration: {array}')
    print(f'sorted array: {array}')
    return array

array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
InsertionSortAlgorithm(array)