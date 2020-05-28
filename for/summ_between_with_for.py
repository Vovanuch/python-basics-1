# summ between, "for" usage
# сумма нечётных чисел в заданном пользователем диапазоне

a = int(input())
b = int(input())

'''
# можно использовать сплит, если планируется ввести значения в одну строку через пробелы.
a, b = input().split()
a = int(a)
b = int(b)
'''

s = 0

for i in range (a, b+1):
	if i % 2 == 1:
		s += i
print(s)
