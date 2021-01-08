'''

Делители-1 🌶️

На вход программе подается два натуральных числа aaa и bbb (a< ba < ba< b). Напишите программу, которая находит натуральное число из отрезка [a; b][a; \, b][a;b] с максимальной суммой делителей.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два числа на одной строке, разделенных пробелом: число с максимальной суммой делителей и сумму его делителей.

Примечание. Если таких чисел несколько, то выведите наибольшее из них.

Sample Input 1:

1
10

Sample Output 1:

10 18

Sample Input 2:

1
100

Sample Output 2:

96 252

'''
# function of finding summ of delitels
def summ_of_delitels(n, list_of_sums):
    s = 0
    for i in range(1, n+1):
        if (n % i) == 0:
            s += i
    # append lists of numbers and sums
    list_of_sums.append(s)

a = int(input().strip())
b = int(input().strip())

# generate lists
list_of_nums = [i for i in range(a, b+1)]
list_of_sums = []

# finding sums and fill list 
for i in range(a, b+1):
    summ_of_delitels(i, list_of_sums)

# reverse lists to start from largest
list_of_nums.reverse()
list_of_sums.reverse()

# finding max of sums, position, and position of number
max_s = max(list_of_sums)
pos_s = list_of_sums.index(max_s)
max_n = list_of_nums[pos_s]
print(max_n, max_s)