'''
Числа Рамануджана 🌶️

Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел. Когда английский математик Годфри Харди навестил его однажды в больнице, он обмолвился, что номером такси, на котором он приехал, было 172917291729, такое скучное и заурядное число. На что Рамануджан ответил: "Нет, нет! Это очень интересное число. Это наименьшее число, выражаемое как сумма двух кубов двумя разными способами". Другими словами: 1729 =13+123=93+103.1729 = 1^3 + 12^3 = 9^3 + 10^3.1729 =13+123=93+103.

Напишите программу, которая находит аналогичные интересные числа. В ответе запишите первые 5 чисел в порядке возрастания, включая число 172917291729.
'''

count_nums = 0
n = 50
list_n = [i for i in range(1, n+1)]
list_cubes = [i**3 for i in range(1, n+1)]
list_sum_cubes = []
list_sum_cubes_all = []

#for i in range(n):
for i in range(n):
    list_sum_cubes.append([])
    list_sum_cubes[i] = [(i+1)**3 + (j)**3 for j in range(1, n+1)]
    
for i in range(n):
    for j in range(n):
        list_sum_cubes_all.append(list_sum_cubes[i][j])
        
#print(*list_sum_cubes, sep='\n')  
list_uniq_raman = []
print('\n'*2)
for c in list_sum_cubes_all:
    #print(c, sep=' ')
    if (list_sum_cubes_all.count(c) > 2) and (c not in list_uniq_raman):
        list_uniq_raman.append(c)

print(*sorted(list_uniq_raman))

#while count_nums < 6:
#    for i in range (2)
#    count_nums += 1