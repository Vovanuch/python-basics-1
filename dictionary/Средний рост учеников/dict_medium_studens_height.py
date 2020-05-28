'''

Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.

Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост

Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.

Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк, например:

Sample Input:

6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153

Sample Output:

1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0

'''
def fillClassesBase(d):
	for i in range(1,12):
		d[i] = 0.0
	return d


lines = []
dicHeight, dicCount = {}, {}

with open('dataset_3380_5.txt') as inf:
	for line in inf:
		lines.append(line.strip().split('	'))
		
#print(lines)
	
dicHeight = fillClassesBase(dicHeight)
dicCount = fillClassesBase(dicCount)
#print(dic)

for line in lines:
	dicCount[int(line[0])] += 1
	dicHeight[int(line[0])] += int(line[2])

#print('dicCount:', dicCount.items())
#print('dicHeight:', *dicHeight.items())

for i in range(1, len(dicHeight)+1):
	if (dicHeight[i] != 0):
		dicHeight[i] = dicHeight[i] / dicCount[i]
	else:
		dicHeight[i] = '-'
		
with open('height_result.txt', 'w') as out:
	for key, value in dicHeight.items():
		#print(key, value)
		out.write(str(str(key) + ' ' + str(value) + '\n'))

