''' sh module usage'''

import sh
#from sh import *

print(sh.pwd())
print(sh.whoami())
my_new_directory = 'my_new_dir_from_script'
sh.mkdir(my_new_directory)
sh.touch(f'{my_new_directory}/my_new_file.txt')
