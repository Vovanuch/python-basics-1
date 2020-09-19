import sys
print('Let\'s ceck python version!')
print('python version is:', sys.version)
print('\nAnother presentation:')
print('python version:', sys.version_info)
print('\n3rd way:')
print(f'You use py version {sys.version_info[0]}!')

if sys.version_info >= (3, ):
    print(f'Congratulations! Your major py version is: {sys.version_info.major}')