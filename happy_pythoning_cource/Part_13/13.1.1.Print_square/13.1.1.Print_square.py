'''

Звездный прямоугольник 1

Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×1014 \times 1014×10 в соответствии с образцом:

**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********

Примечание. Для вывода прямоугольника используйте цикл for.  
'''

def to_print_horizontal_border():
    print('**********')

def to_print_vertical_border(rows):
    for _ in range(rows):
        print('*        *')

to_print_horizontal_border()
to_print_vertical_border(12)
to_print_horizontal_border()