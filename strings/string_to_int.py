s = '123asd456'
new_s = ''
arr_int = []
print(f'Lets int-ing {s}-string! At least, part of it.')
for i in s:
    try:
        arr_int.append(int(i))
        new_s += i
    except:
        print(f'{i} is not a digit. I skip it.')

print('List of digits is:', *arr_int)
print('New line is:', new_s)

print()
print('Second way. Map usage.')
       
try:
    arr_n = map(int, new_s)
except:
    print('Something goes wrong..')
print('New list:', *arr_n)
print(f'Whole digit: {int(new_s)}')

print()
print('3rd way. Map and lamdba usage.')
try:
    arr_m = filter(lambda x : x.isdigit(), s)
    
print(f'3rd array: {arr_m}')