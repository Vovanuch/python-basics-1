#requests

import requests
#r = requests.get('https://api.github.com/events')
#r = requests.get('https://httpbin.org/get')
r = requests.get('http://example.com')

#print(r.json())
#print(r.text)
#print(r.status_code)
#print(r)
#print(r.headers)

#print(r.text)

url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}

r = requests.get(url, params = par)
print(r.text)

print(r.url)

