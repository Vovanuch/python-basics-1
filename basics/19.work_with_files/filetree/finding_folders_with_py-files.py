'''
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py". 

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
'''
import shutil
import os

list_of_dirs = []

# what dir we whant to inspect
checking_dir = 'main'

# what kind of file we want to find
checking_string = '.py'

# Go recurcively thru the selected dir
for curr_dir, dirs, files in os.walk(checking_dir):
    for file in files:
        print(f'we analyse {file} in {curr_dir}')
        if file[-3::1] == '.py':
            print(f'{file} is OK for us! Save {curr_dir} in list')
            if curr_dir not in list_of_dirs:
                list_of_dirs.append(curr_dir)
            
list_of_dirs.sort()
print(list_of_dirs)

# writing finded dirs as a result to file
with open('main_ans.txt', 'w') as out:
    for dir in list_of_dirs:
        out.write(f'{dir}\n')