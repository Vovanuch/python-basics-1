'''

Сортировка трёх 🌶️

Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подается три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.

Sample Input 1:

132
129
135

Sample Output 1:

135
132
129

Sample Input 2:

150
160
156

Sample Output 2:

160
156
150

Sample Input 3:

161
139
148

Sample Output 3:

161
148
139

'''

nums = []
for i in range(3):
    nums.append(int(input().strip()))
    
nums2 = sorted(nums, reverse=True)
print(*nums2, sep='\n')

# 2nd way:
# average = sum(nums) - max(nums) - min(nums)
# print(max, average, min, sep='\n')