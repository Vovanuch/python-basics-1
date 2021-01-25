'''

Корректный ip-адрес

На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу, которая определяет является ли введенная строка текста корректным ip-адресом.

Формат входных данных
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.

Формат выходных данных
Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.

Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.

Sample Input 1:

192.168.0.3

Sample Output 1:

ДА

Sample Input 2:

192.168.0.300

Sample Output 2:

НЕТ

'''
list_s = input().strip().split('.')
is_ip_correct = 'ДА'
for octet in list_s:
    if (int(octet) > 255) or (int(octet) < 0):
        is_ip_correct = 'НЕТ'
        break
    
print(is_ip_correct)