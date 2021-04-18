'''


In the given string find the longest word and output it.

Input data

Given a string in a single line. Words in the string are separated by a single space.

Output data

Output the longest word. If there are several such words, you should output the one, which occurs earlier.

Sample Input:

Everyone of us has all we need

Sample Output:

Everyone

'''
dict_len_words = {}
list_words = input().strip().split()

for w in list_words:
    dict_len_words[w] = len(w)
    
max_len_word = max(dict_len_words.values())
for k, v in dict_len_words.items():
    if v == max_len_word:
        print(k)
        break