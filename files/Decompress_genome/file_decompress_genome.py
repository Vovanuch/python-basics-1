'''
Распаковка строки генома. 


На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

Sample Input:

a3b4c2e10b1

Sample Output:

aaabbbbcceeeeeeeeeeb

'''

with open('dataset_3363_2.txt')as f1:
	s = f1.readline().strip()
	
print(s)

#тестовая строка
#s = 'a11b2c4d5a1c3a2'
print('s:', s)

#объявляем списки и пр места, где будем хранить данные
lst = []
lstind = []
lstinddif = []
result = []

#получаем только буквы из строки
for i in range(len(s)):
	if 	(s[i].isalpha()):		#(s[i] >= 'a') and (s[i]<='z'):
		print(s[i], 'is a symbol!')
		# добавляем в список с буквами
		lst.append(s[i])
		# добавляем индексы букв
		lstind.append(i)
	
#print('lst', lst)
#print('lstind', lstind)

#Получаем цифры из строки, копируя части строки s
for i in range(len(lstind)):
	if i < (len(lstind) -1):
		lstinddif.append(s[lstind[i]+1:lstind[i+1]])

lstinddif.append(s[lstind[-1]+1:len(s)])
#print('lstinddif',lstinddif)

# переводим из строк в целые числа
for i in lstinddif:
	i = int(i)

#вывод итоговой строки
with open('dataset_result.txt', 'w') as out:
	for i in range(len(lst)):
	#print(str(lst[i])+lstinddif[i],end = '')
	#print(lst[i]*lstinddif[i])
		for j in range(int(lstinddif[i])):
			out.write(lst[i])
			#result += lst[i]
			#print(lst[i], end = '')
	
'''
if ('c' > 'b'):
	print('y')
else:
	print('n')
'''
