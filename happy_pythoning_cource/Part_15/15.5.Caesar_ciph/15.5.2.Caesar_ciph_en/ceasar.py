
alphabet_en = 'abcdefghijklmnopqrstuvwxyz' # Строчные буквы

def cesar_gen(my_text, all_symbols, key):
    secret_text = ''
    for c in my_text.lower():
        if c in all_symbols.lower():
            
            i = all_symbols.lower().index(c)
            ciph_i = (i + key) % len(all_symbols)
            secret_text += all_symbols.lower()[ciph_i]
        else:
            secret_text += c
        
    
    return secret_text
    

def set_up_low_char(open_str, sec_str):
    res = ''
    for i in range(len(open_str)):
        #print(open_str[i], sec_str[i])
        if open_str[i].upper() == open_str[i]:
            res += sec_str[i].upper()
            #print(res)
        else:
            res += sec_str[i]
            
    return res
