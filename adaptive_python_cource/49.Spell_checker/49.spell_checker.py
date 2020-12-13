'''


The simplest spell checker is based on a list of known words. Every word in the checked text is searched for in this list and, if such a word was not found, it is marked as erroneous.

Write this spell checker.

The first line of the input contains d d d – number of records in the list of known word. Next go d d d lines contain one known word per line, next — the number l l l of lines of the text, after which — l l l lines of the text.

Write a program that outputs those words from the text, which are not found in the dictionary (i.e. erroneous). Your shell checker should be case insensitive. The words are entered in an arbitrary order. Words, which are not found in the dictionary, should not be duplicated in the output.

Sample Input:

3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa

Sample Output:

aba
c
aaa
aab

'''

n_words = int(input().strip())
list_words = []
for i in range(n_words):
    list_words.append(input().strip().lower())
    
str_count = int(input().strip())
#print(list_words)

# get inputed text. Put in list of lists
list_text = []
for i in range(str_count):
    list_text.append(input().strip().lower().split())
#print(list_text)

# create one list of inputed words from list of lists
list_text_words = []
for elem in list_text:
    for j in elem:
        list_text_words.append(j)
        
list_text_words = sorted(list(set(list_text_words)))

# print words that are not in dictionary 
for i in list_text_words:
    if i not in list_words:
        print(i)