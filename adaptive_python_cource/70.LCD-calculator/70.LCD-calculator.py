'''


Given a sequence of digits, write a program, which outputs these digits in the style of an LCD-calculator (see example).

The size of all digits is 4 symbols in width and 7 symbols in height. There should be one empty column between the digits in the output. There should be no spaces before the first digit.

Digits in the output should be framed, corners of this frame should contain the x symbols, a horizontal line if created by the - symbol ("hyphen"), and the vertical one -- by the vertical line symbol: |.

Input format:
A line of any length (at least one character), comprising a sequence of digits.

Output format:
9 lines containing the digits in the specified style.

Sample Input:

0123456789

Sample Output:

x-------------------------------------------------x
| --        --   --        --   --   --   --   -- |
||  |    |    |    | |  | |    |       | |  | |  ||
||  |    |    |    | |  | |    |       | |  | |  ||
|           --   --   --   --   --        --   -- |
||  |    | |       |    |    | |  |    | |  |    ||
||  |    | |       |    |    | |  |    | |  |    ||
| --        --   --        --   --        --   -- |
x-------------------------------------------------x

'''

def draw_border_h(n):
    # 4n - for every symbol
    # n-1 - for spaces between symbols
    print('x' + '-'*(4*n) + '-'*(n-1) + 'x')
    
    
    
def initialize_rows_and_vert_borders(n):
    list_hor = []
    for i in range(7):
        s = '|' + ' '*4*n + ' '*(n-1) + '|'
        #print(s)
        list_hor.append(list(s))
    return list_hor

def draw_top_cover(list_rows, pos):
    # top cover
    list_rows[0][1+1+pos*4+pos] = '-'
    list_rows[0][1+2+pos*4+pos] = '-'  
    return list_rows

def draw_bottom_cover(list_rows, pos):
    # top cover
    list_rows[6][1+1+pos*4+pos] = '-'
    list_rows[6][1+2+pos*4+pos] = '-'  
    return list_rows

def draw_middle_planka(list_rows, pos):
    # middle
    list_rows[3][1+1+pos*4+pos] = '-'
    list_rows[3][1+2+pos*4+pos] = '-'
    return list_rows

def draw_top_right(list_rows, pos):
    # top-right part
    list_rows[1][1+3+pos*4+pos] = '|'
    list_rows[2][1+3+pos*4+pos] = '|'
    return list_rows

def draw_top_left(list_rows, pos):
    # top-right part
    list_rows[1][1+0+pos*4+pos] = '|'
    list_rows[2][1+0+pos*4+pos] = '|'
    return list_rows

def draw_bottom_rigth(list_rows, pos):
    # bottom-left part
    list_rows[4][1+3+pos*4+pos] = '|'
    list_rows[5][1+3+pos*4+pos] = '|'
    return list_rows

def draw_bottom_left(list_rows, pos):
    # bottom-left part
    list_rows[4][1+0+pos*4+pos] = '|'
    list_rows[5][1+0+pos*4+pos] = '|'
    return list_rows
    

    
    
def draw_0(list_rows, pos):
    # top cover
    list_rows = draw_top_cover(list_rows, pos)
    # top-right part
    list_rows = draw_top_right(list_rows, pos)
    # top-left part
    list_rows = draw_top_left(list_rows, pos)    
    # bottom-left part
    list_rows = draw_bottom_left(list_rows, pos)
    # bottom-right part
    list_rows = draw_bottom_rigth(list_rows, pos)
    # bottom cover 
    list_rows = draw_bottom_cover(list_rows, pos)
    return list_rows

    
def draw_1(list_rows, pos):
    # top-right part
    list_rows = draw_top_right(list_rows, pos)   
    # bottom-right part
    list_rows = draw_bottom_rigth(list_rows, pos)
    return list_rows

def draw_2(list_rows, pos):
    # top cover
    list_rows = draw_top_cover(list_rows, pos)
    # top-right part
    list_rows = draw_top_right(list_rows, pos)
    # middle
    list_rows = draw_middle_planka(list_rows, pos)
    # bottom-left part
    list_rows = draw_bottom_left(list_rows, pos)
    # bottom cover
    list_rows = draw_bottom_cover(list_rows, pos)
    return list_rows


def draw_3(list_rows, pos):
    # top cover
    list_rows = draw_top_cover(list_rows, pos)
    # top-right part
    list_rows = draw_top_right(list_rows, pos)
    # middle
    list_rows = draw_middle_planka(list_rows, pos)
    # bottom-left part
    list_rows = draw_bottom_rigth(list_rows, pos)
    # bottom cover
    list_rows = draw_bottom_cover(list_rows, pos)
    return list_rows

    
def draw_4(list_rows, pos):
    # top-left part
    list_rows = draw_top_left(list_rows, pos)   
    # top-right part
    list_rows = draw_top_right(list_rows, pos)   
    # middle
    list_rows = draw_middle_planka(list_rows, pos)
    # bottom-right part
    list_rows = draw_bottom_rigth(list_rows, pos)
    return list_rows

def draw_5(list_rows, pos):
    # top cover
    list_rows = draw_top_cover(list_rows, pos)
    # top-left part
    list_rows = draw_top_left(list_rows, pos)
    # middle
    list_rows = draw_middle_planka(list_rows, pos)
    # bottom-left part
    list_rows = draw_bottom_rigth(list_rows, pos)
    # bottom cover
    list_rows = draw_bottom_cover(list_rows, pos)
    return list_rows

def draw_6(list_rows, pos):
    # top cover
    list_rows = draw_top_cover(list_rows, pos)
    # top-left part
    list_rows = draw_top_left(list_rows, pos)
    # middle
    list_rows = draw_middle_planka(list_rows, pos)
    # bottom-left part
    list_rows = draw_bottom_left(list_rows, pos)
    # bottom-right part
    list_rows = draw_bottom_rigth(list_rows, pos)
    # bottom cover
    list_rows = draw_bottom_cover(list_rows, pos)
    return list_rows

def draw_7(list_rows, pos):
    # top cover
    list_rows = draw_top_cover(list_rows, pos)
    # top-right part
    list_rows = draw_top_right(list_rows, pos)   
    # bottom-right part
    list_rows = draw_bottom_rigth(list_rows, pos)
    return list_rows


def draw_8(list_rows, pos):
    # top cover
    list_rows = draw_top_cover(list_rows, pos)
    # top-left part
    list_rows = draw_top_left(list_rows, pos)
    # top-right part
    list_rows = draw_top_right(list_rows, pos)
    # middle
    list_rows = draw_middle_planka(list_rows, pos)
    # bottom-left part
    list_rows = draw_bottom_left(list_rows, pos)
    # bottom-right part
    list_rows = draw_bottom_rigth(list_rows, pos)
    # bottom cover
    list_rows = draw_bottom_cover(list_rows, pos)
    return list_rows


def draw_9(list_rows, pos):
    # top cover
    list_rows = draw_top_cover(list_rows, pos)
    # top-left part
    list_rows = draw_top_left(list_rows, pos)
    # top-right part
    list_rows = draw_top_right(list_rows, pos)
    # middle
    list_rows = draw_middle_planka(list_rows, pos)
    # bottom-right part
    list_rows = draw_bottom_rigth(list_rows, pos)
    # bottom cover
    list_rows = draw_bottom_cover(list_rows, pos)
    return list_rows

def draw_empty():
    1

def draw_rows(list_rows):
    for i in list_rows:
        print(*i, sep='')
    #print()


    
string_digits = input().strip()
n = len(string_digits)
dict_functions = {'0':'draw_0', '1':'draw_1', '2':'draw_2', '3':'draw_3', '4':'draw_4', '5':'draw_5', '6':'draw_6', '7':'draw_7', '8':'draw_8', '9':'draw_9'}


draw_border_h(n)
list_rows = initialize_rows_and_vert_borders(n)

for i in range(n):
    f = globals()[dict_functions[f'{string_digits[i]}']]
    list_rows = f(list_rows, i)

draw_rows(list_rows)

draw_border_h(n)