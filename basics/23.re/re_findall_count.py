'''
regexp. findall. count
'''

import re

def finditall(p='', s=''):
    r = re.findall(p, s)
    print(f'We find {len(r)} ({r}) items in "{s}" string, that match to "{p}" template.')

s = 'ac abc abbc abbbc abbbbc'

print()
p = r'ab*c'
finditall(p, s)

print()
p = r'ab?c'
finditall(p, s)

print()
p = r'a.c'
finditall(p, s)

print()
p = r'a*c'
finditall(p, s)

print()
p = r'a.*c'
finditall(p, s)

print()
p = r'ab+c'
finditall(p, s)

print()
p = r'ab{2}c'
finditall(p, s)

print()
p = r'ab{2,4}c'
finditall(p, s)

print()
p = r'a[ab]a'
s = 'abaaba'
finditall(p, s)

print()
p = r'a[ab]a'
s = 'abaaba'
finditall(p, s)

print()
p = r'a[ab]+a'
finditall(p, s)

print()
p = r'a[ab]?a'
finditall(p, s)

print()
p = r'a[ab]?b'
finditall(p, s)


print()
p = r'(test)'
s = 'testandtest'
finditall(p, s)

print()
p = r'(test|text)'
s = 'testing'
finditall(p, s)

print()
p = r'(test|text)'
s = 'textos'
finditall(p, s)

print()
p = r'Hello, (abc|text)*'
s = 'Hello, abc!'
finditall(p, s)
m = re.match(p, s)
print(m)
print(m.group())
print(m.group(0))
print(m.group(1))


print()
p = r'(\w+)-\1'
s = 'test-test'
finditall(p, s)
m = re.match(p, s)
print(m)


print()
p = r'(\w+)-\1'
s = 'test-test chow-chow'
finditall(p, s)
m = re.match(p, s)
print(m)
print(m.group())
print(m.group(0))
print(m.group(1))


# IGNORECASE flag allow to be independent from case. Case-insensitive.
print()
p = r'text'
s = 'TEXT'
r = re.findall(p, s, re.IGNORECASE)
print(f'We find {len(r)} ({r}) items in "{s}" string, that match to "{p}" template.')


print()
p = r'(te)*?xt'
s = 'TEXT'
r = re.findall(p, s, re.IGNORECASE | re.DEBUG)
print(f'We find {len(r)} ({r}) items in "{s}" string, that match to "{p}" template.')


print()
p = r'(te)+?xt'
s = 'TEXT'
r = re.findall(p, s, re.IGNORECASE | re.DEBUG)
print(f'We find {len(r)} ({r}) items in "{s}" string, that match to "{p}" template.')
