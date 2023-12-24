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
    # f - first, l - last
    f, l = 0, len(num) - 1
    resultok = False
    while f <= l:
        m = (f + l) // 2
        if num[m] == find_num:
            f = m
            l = f - 1
            p = m
            resultok = True
        elif num[m] < find_num:
            f = m + 1
        else:
            l = m - 1
    if resultok:
        print(f'{find_num} is finded! index {p}')
    else:
        print(f'{find_num} is not found')





    # if find_num == num[0]:
    #     return print(f'{find_num} is finded! index 0')
    # else:
    #     return print(f'{find_num} is not found')

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
    search = 2
    binary_search(search, numbs)
