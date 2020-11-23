'''
regular expressions
'''


import re

print(re.match.__doc__)
print()
print(re.findall.__doc__)
print()
print(re.sub.__doc__)
print()
print(re.search.__doc__)

# match
print()
print()

pattern = r'abcde'
string = '0123abcdef'
match_result = re.match(pattern, string)
print(match_result)
search_result = re.search(pattern, string)
print(search_result)

print()


# search

pattern = r'a[abc]cd'
d = {}
for i in 'abcd':
    d[i] = 'qa' + i + 'cd'
'''s2 = 'aacd'
s3 = 'abcd'
s4 = 'accd'
s4 = 'afcd' '''
print(d)

for key, value in d.items():
    print(key, value)
    res_search = re.search(pattern, value)
    print(res_search)
    if res_search:
        print('We find it with search!')
    else:
        print('Not finded...')


print()
print()


# findall

pattern = r'a[abc]c'
string2 = 'aac, abc, acc, adc'
finded = re.findall(pattern, string2)
print(f'We find {finded} by pattern "{pattern}" in our string "{string2}" ')


# sub

improved_string = re.sub(pattern, 'aXc', string2)
print(f'We replaced substrings by pattern "{pattern}" and get resulted string "{improved_string}"')


# special sumbols, \
print()
print()
string3 = "Do you speak spanish?"
pattern1 = " spanish?"
pattern2 = " spanish\?"

res1 = re.search(pattern1, string3)
print(f"Using {pattern1} in str {string3}: ", res1)

res2 = re.search(pattern2, string3)
print(f"using {pattern2} in str {string3}: ", res2)