#11. Как узнать о том, что в строке содержатся только цифры?

#Существует метод isnumeric(), который возвращает True в том случае, если все символы, входящие в строку, являются цифрами.

print('80000'.isnumeric()) #=> True


#Используя этот метод, учитывайте то, что знаки препинания он цифрами не считает.

print('1.0'.isnumeric()) #=> False
