import random

def get_word(my_list):
    #i = random.choice(my_list)
    return random.choice(my_list).upper()
    

word_list = ['НОС', 'СОН', 'ПОЛ', 'ГАЗ']
print(get_word(word_list))