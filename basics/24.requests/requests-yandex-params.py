import requests

addr = "https://yandex.ru/search/"
parameters = {"text": "Stepik",
              "test": "test1",
              "name": "Name with spaces",
              "list": ["point1", "point2"]
              }
res = requests.get(addr, params=parameters)
print(res.status_code)
print(res.headers["Content-type"])
print(res.url)
print(res.text)