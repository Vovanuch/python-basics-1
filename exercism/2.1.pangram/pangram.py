''' pangram function'''
def is_pangram(sentence=''):

    set1 = set()
    for symb in sentence.lower():
        if (symb >= 'a') and (symb <= 'z'):
            set1.add(symb)    
    #if all 26 symbols are in set, then sentence is pangram
    if len(set1) == 26:
        return True
    return False
    
    

#print(is_pangram('five boxing wizards jump quickly at it'))
