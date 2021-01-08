#4. Как найти индекс первого вхождения подстроки в строку?

#Есть два метода, возвращающих индекс первого вхождения подстроки в строку. Это — find() и index(). У каждого из них есть определённые особенности.

#Метод find() возвращает -1 в том случае, если искомая подстрока в строке не найдена.

print('Wonderful, wonderful world!'.find('wor')) #=> 19
print('The worlds fastest plane'.find('meen')) #=> -1


#Метод index() в подобной ситуации выбрасывает ошибку ValueError.

print('The worlds fastest plane'.index('plane')) #=> 19
print('The worlds fastest plane'.index('car')) #=> ValueError: substring not found
