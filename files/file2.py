'''
запись в файл
'''

f = open('filewrite', 'w')
f.write('Str1 \n')
f.write('СТрока 2 \n')
f.close()

with open('filewrite') as fo:
	for l in fo:
		l = l.strip()
		print(l)

with open('filewrite', 'a') as out:
	out.write('another string \n')
	out.write(str(123))
	
	
with open('filewrite') as fo:
	for l in fo:
		print(l.strip())
		
