'''
# файлы.
'''
f = open('testfile.txt')
s1 = f.readline()
s2 = f.readline()
f.close()
print(s1 + s2)

# функция strip() отрезает технические символы типа \n  \t и др.
with open('testfile.txt', 'r') as inf:
	s3 = inf.readline().strip()
	print(s3)

import os

print(os.path.join('.', 'dirname', 'filename'))

with open('testfile.txt') as f:
	for line in f:
		line = line.strip()
		print(line)
