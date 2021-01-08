'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

'''
import requests

url = ''
folder = 'https://stepic.org/media/attachments/course67/3.6.3/'
fname = ''

with open('dataset_3378_3.txt') as addr:
	url = addr.readline().strip()
	
print(url)

r = requests.get(url)

'''
if ('We' not in r.text):
	print('go to another url!')
	print(r.text)

s = 'We are here!'
p = s.find('We')
print(p)
'''

#while r.text.find('We') != 0: # нормальное условие, всё работает. Если позиция слова "We" не является самой первой или не находится вообще
#Проверяем второй способ, через вхождение (in)
while 'We' not in r.text:
	print('go to another url')
	url = folder+r.text.strip()
	print(url)	
	r = requests.get(url)
	
print (r.text)

with open('resultfile.txt', 'w') as out:
	out.write(str(r.text))
