#requests
'''
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.

Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям).

После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода splitlines.

В поле ответа введите одно число или отправьте файл, содержащий одно число.

'''
import requests

#dataset_3378_2.txt
adr = ''
with open('dataset_3378_2.txt') as inf:
	adr = inf.readline().strip()

print(adr)

r = requests.get(adr)
#print(r.text)

listlines = []

listlines = r.text.splitlines()
#print(*listlines)

i = 0

for l in listlines:
	i += 1
	
with open('linescount.txt', 'w') as res:
	res.write(str(i))
	
print(i)
