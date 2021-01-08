'''
requests and format
'''

import requests

template = "We get responce from {0.url} with status {0.status_code}"
r = requests.get('https://www.python.org')
print(r.status_code)
print(r.content)
print(template.format(r))

