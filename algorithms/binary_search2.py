# binary search

def binary_search(my_list):
    if (len(my_list) == 2):
        ans = input(f'Is your number a {my_list[0]}? y/n: ')
        if ans.lower == 'y':
            print(f'Thanks, your number is {my_list[0]}!')
            return
        else:
            print(f'Thanks, your number is {my_list[1]}!')
            return
            
    my_min = min(my_list)
    my_max = max(my_list)
    mid = (my_min + my_max) // 2
    ans = input(f'Is your number in range between {my_min} and {mid}? y/n: ').strip()
    if (ans.lower() == 'y'):
        my_list = [i for i in range(my_min, mid+1)]
        #print(my_min, mid+1)
    elif (ans.lower() == 'n'):
        my_list = [i for i in range(mid, my_max+1)]
        #print(mid, my_max+1)
    else:
        print('Your answer is incorrect. Try again!')
    
    binary_search(my_list)    
        
    
print('This is magic search machine! \nPlease, set borders of range: ')
bot = input('Bottom:')
top = input('Top:')
print('Make a wish about integer number in your ming')

list_n = [i for i in range(int(bot), int(top)+1)]
binary_search(list_n)