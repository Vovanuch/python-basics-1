'''
os.path является вложенным модулем в модуль os, и реализует некоторые полезные функции для работы с путями.

os.path.abspath(path) - возвращает нормализованный абсолютный путь.

os.path.basename(path) - базовое имя пути (эквивалентно os.path.split(path)[1]).

os.path.commonprefix(list) - возвращает самый длинный префикс всех путей в списке.

os.path.dirname(path) - возвращает имя директории пути path.

os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла.

os.path.expanduser(path) - заменяет ~ или ~user на домашнюю директорию пользователя.

os.path.expandvars(path) - возвращает аргумент с подставленными переменными окружения ($name или ${name} заменяются переменной окружения name). Несуществующие имена не заменяет. На Windows также заменяет %name%.

os.path.getatime(path) - время последнего доступа к файлу, в секундах.

os.path.getmtime(path) - время последнего изменения файла, в секундах.

os.path.getctime(path) - время создания файла (Windows), время последнего изменения файла (Unix).

os.path.getsize(path) - размер файла в байтах.

os.path.isabs(path) - является ли путь абсолютным.

os.path.isfile(path) - является ли путь файлом.

os.path.isdir(path) - является ли путь директорией.

os.path.islink(path) - является ли путь символической ссылкой.

os.path.ismount(path) - является ли путь точкой монтирования.

os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.

os.path.normcase(path) - нормализует регистр пути (на файловых системах, не учитывающих регистр, приводит путь к нижнему регистру).

os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на предыдущие директории. На Windows преобразует прямые слеши в обратные.

os.path.realpath(path) - возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).

os.path.relpath(path, start=None) - вычисляет путь относительно директории start (по умолчанию - относительно текущей директории).

os.path.samefile(path1, path2) - указывают ли path1 и path2 на один и тот же файл или директорию.

os.path.sameopenfile(fp1, fp2) - указывают ли дескрипторы fp1 и fp2 на один и тот же открытый файл.

os.path.split(path) - разбивает путь на кортеж (голова, хвост), где хвост - последний компонент пути, а голова - всё остальное. Хвост никогда не начинается со слеша (если путь заканчивается слешем, то хвост пустой). Если слешей в пути нет, то пустой будет голова.

os.path.splitdrive(path) - разбивает путь на пару (привод, хвост).

os.path.splitext(path) - разбивает путь на пару (root, ext), где ext начинается с точки и содержит не более одной точки.

os.path.supports_unicode_filenames - поддерживает ли файловая система Unicode.
'''

import os.path

print('Full path is: \n', os.path.abspath("."))
print()
name = 'test.txt'
print(f'Is the {name} a file?', os.path.isfile(name))
print(f'Is the {name} a directory?', os.path.isdir(name))

print()
print('Lets create folders!')
try:
    os.makedirs('./testdir1/testdir2/testdir3')
except Exception:
    print("Cant create dirs. May be they exists yet?")
else:
    print('Dirs are created!')
finally:
    print("Thank you for using Vova's Soft Lab! =)")
    
print()
print()
#print(print(os.environ) ) # словарь переменных / dictionary of environment variables
print(f'os.environ["PATH"] is {os.environ["PATH"] }') 


print()
# work with getenv
print('os.getenv function says:', os.getenv("TMP"))


print()
# makedirs again. REplace and recreate folders even if they exists. Files are holded, not removed.
my_path = r'/home/vladimir/Programming/Python/scripts/basics/19.work_with_files/testdir2/testdir3'
try:
    os.makedirs(my_path, exist_ok=True)
except Exception:
    print('Something goes wrong.. Check your code, please!')
else:
    print('Folders in my_path created!')
finally:
    print('Bye! Great to see you again!')


print()
print()
# isdir ans isfile
what_to_check = input('Please, enter a name of file or directory: ')
print('Is {what_to_check} a file?', os.path.isfile(what_to_check))
print('Is {what_to_check} a dir?', os.path.isdir(what_to_check))
