from random import randint

def bubble_sort(num):
    n = len(num)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num

def selection_sort(num):
    n = len(num)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if num[j] < num[min_index]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    return num

def binary_search(find_num, num):
    low, high = 0, len(num) - 1
    while low <= high:
        mid = (low + high) // 2
        if num[mid] == find_num:
            return mid
        elif num[mid] < find_num:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbs = []
for i in range(1, 11):
    numbs.append(randint(1,100))
menu = input('bubble sort or selection sort? ')
if menu == 'bubble':
    sorted_list = bubble_sort(numbs)
elif menu == 'selection':
    sorted_list = selection_sort(numbs)
else:
    print('coomand is not found')
if menu == 'bubble' or menu == 'selection':
    print("Sorted List:", sorted_list)

    element_to_search = 10
    result = binary_search(element_to_search, sorted_list)
    print(f"Binary Search: Element {element_to_search} found at index {result}" if result != -1 else f"Element {element_to_search} not found")