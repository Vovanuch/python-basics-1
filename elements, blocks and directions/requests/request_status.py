'''
requests 2
'''
#!/usr/bin/python3

import requests

r = requests.get('https://www.python.org')
print(r.url, r.status_code)

r2 = requests.get("https://ya.ru")
print(r2.url, r2.status_code)
print(r2.text)
print(r2.headers)
