'''


Write a program that checks whether two given words are anagrams.

The program should output True in the case if entered words are anagrams, and False otherwise.

Input format:

Two words, each on a separate line. Words can only consist of Latin characters. Your solution should be case insensitive, i.e. characters' case should not affect the answer.

Sample Input 1:

silent
listen

Sample Output 1:

True

Sample Input 2:

AbaCa
AcaBa

Sample Output 2:

True

Sample Input 3:

abaca
acada

Sample Output 3:

False

'''

word1, word2 = input().strip().lower(), input().strip().lower()
is_anagram = False
if len(word1) == len(word2):
    inclusion_count = 0
    for i in word1:
        if (i in word2) and (word1.count(i) == word2.count(i)) :
            inclusion_count += 1
    if inclusion_count == len(word2):
        is_anagram = True
    
print(is_anagram)