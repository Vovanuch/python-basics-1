''' pangram function'''
def is_pangram(sentence=''):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    result = True
    #initializing alphabet dictionary
    dic = {}
    for a in alp:
        dic[a] = 0

    #counting symbols is string
    for symb in sentence.lower():
        if (symb >= 'a') and (symb <= 'z'):
            dic[symb] += 1
    
    #Try to find zero in count. If yes, it means that symbol is missing and sentence isn't pangram
    for val in dic.values():
        if val == 0:
            result = False
            
    return result


