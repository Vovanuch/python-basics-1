import requests

res = requests.get("https://ya.ru")
print(res.headers)

print(res.status_code)

print(res.headers['Content-type'])

print(res.content)
print(res.text)