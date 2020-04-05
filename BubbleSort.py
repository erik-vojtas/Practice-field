#Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

def BubbleSort(list):
    temp = 0
    sorted_list = sorted(my_list)
    count = 0
    while my_list != sorted_list:
        for i in range(0, len(my_list)-1):
            if my_list[i] > my_list[i+1]:
                temp = my_list[i+1]
                my_list[i+1] = my_list[i]
                my_list[i] = temp
                my_list[i] = my_list[i]
            else:
                my_list[i] = my_list[i]
        count += 1
    print(f'Sorted list = {my_list}, pass(es) = {count}.')


my_list = [13, 2, 9, 4, 18, 45, 37, 63]
BubbleSort(my_list)