'''
Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1 разделённую на общее количество всех чисел.'''



def get_flat(my_old_list, my_new_list):
    for elem in my_old_list:
        if isinstance(elem, list):
            get_flat(elem, my_new_list)
        else:
            my_new_list.append(elem)
    return my_new_list


list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

list2 = []
list2 = get_flat(list1, list2)

total = sum(list2)
mean = total / len(list2)

print(mean)