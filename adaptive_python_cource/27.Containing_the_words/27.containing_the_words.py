'''


Input of the program is a line containing the words separated by a space. The program should output the information of lengths of words in the given line, from the shortest to the longest word (see the example).

A word is a sequence of arbitrary characters surrounded by spaces or line boundaries. Note that punctuation marks also belong to a word.

Input format:
A string containing a sequence of Latin characters and punctuation marks, separated by a space.

Output format:
For each word length that appears in the original string, you need to specify the number of words with such length in a format:

length: amount


Output this information in the order of increasing length.

Sample Input:

Beautiful is better than ugly. Explicit is better than implicit.

Sample Output:

2: 2
4: 2
5: 1
6: 2
8: 1
9: 2

'''

try:
    list_words = input().strip().split()
    #print(list_words)
    list_len = []
    d1_lens = dict()
    
    for w in list_words:
        list_len.append(len(w))
    
    #print(list_len)    
    list_len_uniq = sorted(list(set(list_len)))
    #print(list_len_uniq)
    
    for i in list_len_uniq:
        d1_lens[i] = list_len.count(i)
        
    #print(d1_lens)
    
    for k, v in d1_lens.items():
        print(f'{k}: {v}')
    
except:
    print('Incorrect input')