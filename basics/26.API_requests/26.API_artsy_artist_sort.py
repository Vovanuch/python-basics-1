'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.

Работа с API Artsy

Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), и в дальнейшем все запросы к API осуществляются при помощи этого ключа.

Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.

После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, как можно выполнить запрос и как выглядит ответ сервера
'''


import requests
import json


def get_list_from_file(file_name):
    my_list = list()
    with open(file_name, 'r') as inf:
        lines = inf.readlines()
        for line in lines:
            my_list.append(line.strip())
    return my_list

def get_token_from_artsy(client_id, client_secret):
    # инициируем запрос на получение токена
    r = requests.post('https://api.artsy.net/api/tokens/xapp_token', 
                      data = {
                          "client_id": client_id,
                          'client_secret': client_secret
                      })
    
    # разбираем ответ сервера
    j = json.loads(r.text)
    
    # достаём токен
    token = j['token']    
    return token
    

# Client Id 	2ff741f03a4acdf53746
# Client Secret 	63278dd6e4ffa6fd1349ce7b648508d5
# to get token: "https://api.artsy.net/api/tokens/xapp_token?client_id=2ff741f03a4acdf53746&client_secret=63278dd6e4ffa6fd1349ce7b648508d5"

def get_info_about_artists(token, list_of_artists_id):
    # словарь имён и дат рождения
    dict_name_year_artist = dict()
    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token" : token}
    # инициируем запрос с заголовком в цикле
    for i in list_of_artists_id:
        url = f"https://api.artsy.net/api/artists/{i}"
        #print(url)
        r = requests.get(url, headers=headers)
        # разбираем ответ сервера
        j = json.loads(r.text)
        dict_name_year_artist[j['sortable_name']] = j['birthday']
        #print(j)
        #print(j['sortable_name'])
        #print(j['birthday'])
    return dict_name_year_artist
    
def sort_dict_by_value(my_dict):
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    return sorted_dict
    
def set_list_to_file(file_name, my_list):
    with open(file_name, 'w') as ouf:
        for i in my_list:
            ouf.write(i+'\n')


client_id = '2ff741f03a4acdf53746'
client_secret = '63278dd6e4ffa6fd1349ce7b648508d5'

# считываем список идентификаторв из файла
list_artists = get_list_from_file("dataset_24476_4.txt")
print(list_artists)

# формируем токен
token = get_token_from_artsy(client_id, client_secret)
# получаем информацию с сайта на основе токена и списка идентификаторов, формируем словарь
dict_artists = get_info_about_artists(token, list_artists)
print(dict_artists)

# сортируем словарь по значениям (годам рождения)
dict_sorted_artists = dict(sorted(dict_artists.items(), key=lambda item: item[1])) #sort_dict_by_value(dict_artists)
print(dict_sorted_artists)

# формируем список из ключей словаря
list_sorted_artists = list(dict_sorted_artists.keys())

# записываем список в файл
set_list_to_file("sorted_artists.txt", list_sorted_artists)
print(list_sorted_artists)

'''
# инициируем запрос на получение токена
r = requests.post('https://api.artsy.net/api/tokens/xapp_token', 
                  data = {
                      "client_id": client_id,
                      'client_secret': client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаём токен
token = j['token']

'''
'''
Теперь все готово для получения информации о художниках. На стартовой странице документации есть пример того, как осуществляется запрос и как выглядит ответ сервера. Пример запроса на Python.
'''
'''
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)
print(j)
print(j['sortable_name'])
print(j['birthday'])
'''
