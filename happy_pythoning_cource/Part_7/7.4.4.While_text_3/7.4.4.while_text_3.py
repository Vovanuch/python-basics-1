'''

Количество членов

На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). Напишите программу, которая выводит общее количество членов данной последовательности.

Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.

Формат выходных данных
Программа должна вывести общее количество членов данной последовательности.

Sample Input 1:

Skyrim
GTA
Mafia
стоп
Battlefield

Sample Output 1:

3

Sample Input 2:

Yandex
Google
Opera
Safari
хватит
Mozilla

Sample Output 2:

4

Sample Input 3:

Skype
Viber
Telegram
WhatsApp
Discord
достаточно

Sample Output 3:

5

'''

stop_list = ['стоп', 'хватит', 'достаточно']
words_list = []
text = input().strip()
while text not in stop_list:
    words_list.append(text)
    text = input().strip()

#print(*words_list, sep='\n')
print(len(words_list))

