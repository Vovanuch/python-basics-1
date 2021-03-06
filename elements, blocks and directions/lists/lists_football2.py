'''


Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n n n — количество завершенных игр.
После этого идет n n n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6




'''

#находим неповторяющиеся команды и формируем из них словарь(ключ = название) с пока пустыми значениями value
def findTeam(arr, d):
	#d = dict()
	for i in arr:
		if not(i.isdigit()):
			d[i] = [0,0,0,0,0]

	return d

#считаем количество игр команды, записываем в словарь
def countGames(arr, d):
	for key in d.keys():
		d[key][0] = arr.count(key)		
		
	return d

#считаем победы, ничьи, поражения и очки для каждой команды
def countAll(arr, d):
	for game in arr:
		if int(game[1]) > int(game[3]):
			#[][1] - победы
			d[game[0]][1] += 1
			#[][3] - поражения
			d[game[2]][3] += 1
		
			#очки
			d[game[0]][4] += 3
		elif int(game[1]) == int(game[3]):
			#[][2] - ничьи
			d[game[0]][2] += 1
			d[game[2]][2] += 1
		
			#очки
			d[game[0]][4] += 1
			d[game[2]][4] += 1
		elif int(game[1]) < int(game[3]):
			#[][3] - поражения
			d[game[0]][3] += 1
			#[][1] - победы
			d[game[2]][1] += 1
		
			#очки
			d[game[2]][4] += 3
	return d

#выводинм всё на печать в требуемом формате	
def printResult(d):
	for key, val in d.items():
		print(key+':', *val)


d = {}
n = 0
l1 = []
l2 = []
l3 = []

n = int(input())

# получаем списки-массивы. l1 - список списков, l2 - одномерный список
for i in range(n):
	tmp = input().split(';')
	l1.append(tmp)
	l2 += tmp

d = findTeam(l2, d)
d = countGames(l2, d)
d = countAll(l1, d) 
printResult(d)
#print(d)
