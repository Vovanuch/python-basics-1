import os

print(f'Current directory: {os.getcwd()}')
#a = os.walk('.')
print()
#print(*a)

for curr_dir, dirs, files in os.walk('.'):
    print(curr_dir, dirs, files)
    
    
