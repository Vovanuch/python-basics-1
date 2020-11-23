'''

Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru

'''


import requests
import re

def get_links(my_url):
    ''' We get list of links from selected url  '''
    #pattern = r'<a[^>]* href="([^"]*)"'
    pattern = r'<a[^>]* href=["\']([^"#\']*)["\']'
    res = requests.get(my_url)
    text_res = res.text
    list_of_links = re.findall(pattern, text_res)
    return list_of_links

def get_links_from_text(text_for_analysis):
    ''' We get list of links from string or text '''
    #pattern = r'<a[^>]* href="([^"]*)"'
    pattern = r'<a[^>]* href=["\']([^"]*)["\']'
    #res = requests.get(my_url)
    #text_res = res.text
    list_of_links = re.findall(pattern, text_for_analysis)
    return list_of_links


def cut_protocol_from_link(link):
    ''' We get link without protocol '''
    index_of_protocol = link.find('://')
    if (index_of_protocol > -1):
        link = link[index_of_protocol+3:]
    return link

def cut_extend_from_link(link):
    ''' if there is protocol - https, http, ftp - delete it  '''
    index_of_slash = link.find('/')
    if (index_of_slash > -1):
        link = link[:index_of_slash]
    
    ''' if there is a colon with port, may be - delete colon and port  '''
    index_of_colon = link.find(':')
    if (index_of_colon > -1):
        link = link[:index_of_colon]    
    
    ''' if it is relative link - delete this element'''
    index_of_relative = link.find('..')
    if (index_of_relative > -1):
        link = ''     
    
    return link    

def get_domen_from_link(link):
    link = cut_protocol_from_link(link)
    link = cut_extend_from_link(link)
    return link

'''
test_text = 'http://stepic.org/courses'         
test_link = cut_protocol_from_link(test_link)
print(test_link)
test_link = cut_extend_from_link(test_link)
print(test_link)'''




domains_set = set()
domains_list = list()

#'''
point_a = input()
links = get_links(point_a)
for link in links:
    link = get_domen_from_link(link)
    if (link) and (link not in domains_set):
        domains_set.add(link)

'''
with open('html_file', 'r') as inf:
    lines = inf.readlines()
    for line in lines:
        #print('Analysed line is: ', line)
        link = str(*get_links_from_text(line))
        #print('Link for getting domain is:', link)
        link = get_domen_from_link(link)
        if (link) and (link not in domains_set):
            domains_set.add(link)
            #print(link)
#'''


domains_list = list(domains_set)
domains_list.sort()
for i in domains_list:
    print(i)
