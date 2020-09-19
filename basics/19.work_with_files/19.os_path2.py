
import os
import os.path


# current dir:
print(os.getcwd())

# print all files in directory
print()
print(os.listdir(), sep='\n')

# print all files in selected directory
print("\nAll files in selected directory: \n")
print(os.listdir("/"))

# change dir and print new location
print()
print('Go to parent dir')
os.chdir('..') 
print(os.getcwd())
