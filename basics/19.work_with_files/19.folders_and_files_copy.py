import shutil
import os.path

def is_exist(file_name):
    if os.path.exists(file_name):
        print(f'{file_name} is exist!')  
    else:
        print(f'There are no {file_name} here.')

# Copying files

print('Lets copy one file (test2.txt) to another (copy_of_test2.txt)!')
is_exist('copy_of_test2.txt')
    
shutil.copy('test2.txt', 'copy_of_test2.txt')

is_exist('copy_of_test2.txt')


# Copying folders
print()
print('Lets copy whole directory!')
is_exist('copy_of_testdir2')
shutil.copytree('./testdir2', 'copy_of_testdir2')
is_exist('copy_of_testdir2')