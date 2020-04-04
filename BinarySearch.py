#Binary search
#returns num and how many steps it takes

def findNum(searched_num, list):
    steps = 0
    sorted_list = sorted(list)
    start = 0
    end = len(sorted_list)-1
    found = False
    while start <= end and not found:
        mid_point = (start + end) // 2
        if sorted_list[mid_point] == searched_num:
            steps += 1
            found = True
        else:
            if searched_num < sorted_list[mid_point]:
                end = mid_point - 1
                steps += 1
            else:
                start = mid_point + 1
                steps += 1

    return f'The item {searched_num} has been found in {steps} step(s). The position of item {searched_num} in the list is {list.index(searched_num)+1}.'




my_list = [13, 2, 9, 4, 18, 37, 63, 3, 5, 6, 88, 92, 0, 45, 291, 320, 2, 1, 4, 77, 88, 99]
print(findNum(45, my_list))






