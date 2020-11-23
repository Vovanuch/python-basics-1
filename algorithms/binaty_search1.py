'''
binary search 1
'''


def get_borders():
    borders = {}
    borders['bottom'] = input('Please, enter the bottom border of range, integer only: ')
    borders['top'] = input('Please, enter the top border of range, integer only: ')
    
    #if (borders['bottom'].isdigit()) and (borders['top'].isdigit()): 
    try:
        borders['bottom'] = int(borders['bottom'])
        borders['top'] = int(borders['top'])
        if borders['top'] >= borders['bottom']:
            return borders
        else:
            print('Sorry, you enter incorrect borders. Top less than bottom.')
            return 0
    except:
        print('Sorry, you enter incorrect borders. Not a integer number.')
        return 0

def to_int(a):
    try:
        a = int(a)
        return a
    except:
        print(f'Sorry, {a} is not a correct integer number.')


def get_number():
    num_str = input('Please, thinking of a number between entered borders. Enter it! ') 
    num = to_int(num_str)
    return num

def is_correct_number(dic, num):
    if number!=None:
        if dic['bottom'] <= number <= dic['top']:
            return True
    return False




borders = get_borders()
print(borders)
number = get_number()
print(number)

if is_correct_number(borders, number):
    print("Your number is correct. Let's go to the next step!")
else:
    print("Your number is out of range. Try again!")
