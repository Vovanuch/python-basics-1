'''

Кремниевая долина 🌶️🌶️

Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число nnn – количество холодильников. В последующих nnn строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 555 до 100100100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.
Made with 💛 by Anri Tabuev

Sample Input 1:

6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n

Sample Output 1:

1 2 3

Sample Input 2:

9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton

Sample Output 2:

1 2 7 8

Sample Input 3:

1
anton

Sample Output 3:

1

'''
n = int(input().strip())
list_refr = [input().strip().lower() for i in range(n)]
list_anton = ['a', 'n', 't', 'o', 'n']
list_part_anton = ['a', 'an', 'ant', 'anto', 'anton']
list_indexes_anton = []

#print(list_refr)

for i in range(n):
    if all([char in list_refr[i] for char in list_anton]):
        s = ''
        for j in range(len(list_refr[i])):
            if list_refr[i][j] in list_anton:
                s += list_refr[i][j]
        #print(f's = {s}')
        s1 = ''

        for char in s:
            if (s1 + char) in list_part_anton:
                s1 += char
                
        #print(f's1 = {s1}')
        if 'anton' in s1:
            list_indexes_anton.append(i+1)
        

print(*list_indexes_anton)
