'''

Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:

abc a bCd bC AbC BC BCD bcd ABC

Sample Output:

abc 3

'''

lst = []
d = {}
maksN = 0
maksS = ''

with open('dataset_3363_3.txt') as f:
	for line in f:
		#lst.append(line.strip().split())
		lst += line.strip().lower().split()
		
print(*lst)

for i in lst:
	d[i] = lst.count(i)
	
print(d.items())

for key, value in d.items():
	if (maksS == ''):
		maksN = value
		maksS = key
		continue		
	
	if (int(value) == maksN) and (maksS > key):
		maksN = value
		maksS = key
	elif (int(value) > maksN):
		maksN = value
		maksS = key	
		
print(maksS, maksN)

with open('result.txt', 'w') as f:
	f.write(maksS + ' ' + str(maksN))

'''
s1 = 'a'
s2 = 'aba'
if s1 > s2:
	print(f'{s1} >= {s2}')
else:
	print(f'{s1} < {s2}')
'''
