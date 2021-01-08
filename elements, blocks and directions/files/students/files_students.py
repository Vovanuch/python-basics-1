'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам.

В качестве ответа на задание прикрепите полученный файл со средними оценками.

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85

Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''
#список списков, список верхнего уровня - студент со своими оценками
students_lines = []

#список средних оценок студентов
middle = []

# список средних оценок за предмет
middle_lesson = []

# плоский список
students_items = []

# считываем строки из файла построчно
with open('dataset_3363_4.txt') as sl:
	for line in sl:
		students_lines.append(line.strip().split(';'))
		students_items += line.strip().split(';')
		
print(students_lines)
print()

# количество студентов
studentsCount = len(students_lines)
# количество предметов
lessonCount = len(students_lines[0]) - 1

#находим среднюю для студента, записываем в массив middle
for i in range(len(students_lines)):
	s1 = 0
	for j in range (1, len(students_lines[i])):
		s1 += int(students_lines[i][j])
		print('s1 =', str(s1))
	mid = s1 / (len(students_lines[i]) - 1)
	print('mid =', mid)
	middle.append(mid)

print(middle)

print()

#просто вывод табличкой
for i in range(len(students_lines)):
	#s1 = 0
	for j in range (0, len(students_lines[i])):
		print(students_lines[i][j], end = ' ')
	print()

print()
#s2 = 0

# для всех предметов
str_middle_lesson = ''
for j in range(lessonCount):
	s2 = 0
	# по плоскому списку проскакиваем, собираем значение со всех студентов по отдельному предмету
	for i in range(j+1, len(students_items), lessonCount+1):
		print(students_items[i], end = ' ')
		s2 += int(students_items[i])
		
	mid2 = s2 / studentsCount
	print('mid2 =', mid2)
	middle_lesson.append(mid2)
	str_middle_lesson += str(mid2) + ' '
	
print(*middle_lesson)
print(str_middle_lesson)
	
with open('students_result.txt', 'w') as out:
	for i in middle:
		out.write(str(i) + '\n')
	out.write(str_middle_lesson)
