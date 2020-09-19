s = '12345asdf6789'
print(f'Now we form list only with digits from string s: {s}')
list_digits = list(map(int, filter(lambda x : x.isdigit(), s)))
print(*list_digits)
