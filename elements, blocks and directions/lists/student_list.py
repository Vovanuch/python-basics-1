# lists 1. Списки.
students = ["Vladimir", 'Jose', 'Enrico de la Tarde']

for student in students:
	print("Hola,", student + "!")

print("Hola a todos!", len(students), "estudiante(s)!")

for i in range(len(students)):
	print("Buenvenido,", students[i])

print(students[::-1])
print(students[:2])



#summ
maestros = ["Gonsales", "Carlos"]
persons = maestros + students
print(persons)


#append
students += ['Misha', "Sasha'"]
print(students)
students.append('Olga')
print(students)




#insert
students.insert(1, 'Lida')
print(students)

s = ['a']
s += ['b']
# Большая разница между тем, чтобы добавлять ['abc'] и 'abc' !
# При добавлении 'abc' добавляется каждый символ как отдельный элемент
s += 'abc'
print(s)
s += ['abc']
print(s)





# Удаление элементов
# Способ 1
students.remove('Jose')
print(students)
#Способ 2
del students[4]
print(students)

if 'Vladimir' in students:
	ind = students.index('Vladimir')
	print('Vladimir is a student! His index is', ind)


if 'Ivan' not in students:
	print('Ivan not in students list!')




# min and max
print("\nMax studend is", max(students))
print("Min studend is", min(students))



#Сортировка. Order. Sorted.
#sorted() - пишет в новый массив отсортированный текущий, при этом текущий не меняется
ordstudents = sorted(students)
print('\nOrdering new list...')
print(ordstudents)
print('Current students list is:')
print(students)

# sort() - сортирует именно текущий массив.
print('\nOrdering current students list...')
students.sort()
print(students)


# reverse. 3 ways.
# 1st. with changing base
print('\nReversing output:')
students.reverse()
print(students)

# 2nd
print(students[::-1])
print(students)
#revstudents = reversed(students)
#print('\nReversing output:')
#print (revstudents)


# Присвоение списков. 
second_st = students
print(second_st)
second_st[0] = 'New Student!'
print('New second_st is:', second_st)
print('Basic list is:', students, "\n You see, it is modified too!")
