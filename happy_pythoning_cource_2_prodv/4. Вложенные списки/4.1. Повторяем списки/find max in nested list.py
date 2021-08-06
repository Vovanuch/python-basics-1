'''
Дополните приведенный код, используя цикл for и встроенную функцию max(), чтобы он выводил один общий максимальный элемент среди всех элементов вложенных списков list1.
'''

def get_flat(my_old_list, my_new_list):
    for elem in my_old_list:
        if isinstance(elem, list):
            get_flat(elem, my_new_list)
        else:
            my_new_list.append(elem)
    return my_new_list

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

list2 = []

list2 = get_flat(list1, list2)
print(*list2)
maximum = max(list2)

#for elem in list1:
#    pass

print(maximum)