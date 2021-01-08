# Сжатие строки "Кодированием" символов.
'''
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

'''

s = input()
#длина строки
l = len(s)
j=0
cnt = 0

# во внешнем цикле обходим все символы в строке
for i in range(l):
	#сбрасываем в ноль счётчик
	cnt = 0
	
	#для второго и последующих символов проверяем, что текущий символ не равен предыдущему. 
	# Если равен - пропускаем итерацию, так как для пред.символа уже посчитали в предыдущей итерации.  
	if (i>0):
		if (s[i] == s[i-1]):
				continue
	
	#внутренним циклом  j обходим все последующие символы, начиная не с первого, а с i-того
	for j in range(i, l):
		# если i-ый сивмвол равен j-тому, то увеличиваем счётчик. 
		if s[i] == s[j]:
			cnt += 1
		else:
			break
	#выводим получившуюся строку, состоящую из буквы и кол-ва её беспрерывных повторов
	print(s[i]+str(cnt), end ='')

	
	
		
		