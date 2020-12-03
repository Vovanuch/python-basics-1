'''


When Anthony read "War and Peace", he wondered how many words and how much of them were used in this book.

Help Anthony to write a simplified version of a program that can count the words, separated by a space and output the resulting statistics.

The program must read one line from the standard input and for each unique word in this line output the count of its repeated occurrence (case insensitive) in the "word amount" format (see the output example).

The order of words output may be arbitrary. Each unique word must appear in the output only once.

Sample Input 1:

a aa abC aa ac abc bcd a

Sample Output 1:

ac 1
bcd 1
abc 2
aa 2
a 2

Sample Input 2:

a A a

Sample Output 2:

a 3

'''

def lower_list(my_list):
    for i in range(len(my_list)):
        my_list[i] = my_list[i].lower()
    
    return my_list



list_s = input().strip().split()
list_s = lower_list(list_s)
list_s_uniq = list(set(sorted(list_s)))
dict_s = dict()

for i in list_s_uniq:
    dict_s[i] = list_s.count(i)
    
for k, v in dict_s.items():    
    print(k, v)
    