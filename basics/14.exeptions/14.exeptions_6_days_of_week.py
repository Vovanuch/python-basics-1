''' exeptions 6. Days of week  '''

my_dict_days = {1:'Monday', 2: 'Tuesday', 3:'Wensday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
day = input('Please, enter the number of day at week: ')
try:
    #day = int(day)
    print('The name of the day is: ', my_dict_days[int(day)])
except Exception as e:
    print('Your input is not a correct number! Please, use range 1 - 7.')
finally:
    print('Thanks! Bye!')
