'''
str.find
str.startswith
str.endswith
'''
s = '9fancvt0abcdegasg'
print('Is there abc string?')
print('abc' in s)
print('Index of position is', s.find('abc'))
print()
print(str.find.__doc__)

print('Is there dsa string?')
print('dsa' in s)
print('Index of position is', s.find('dsa'))
print()

print()
s1 = "We are the champions, my friend!"
s2 = "We are"
s3 = "Master"
print('Is s2 the beginning of s1?', s1.startswith(s2))
print('Is s3 the beginning of s1?', s1.startswith(s3))

print(str.startswith.__doc__)

# we can use tuple instead of single str. If at least one is the beginning, function will return true.
print('Is s3, s3 the beginning of s1?', s1.startswith((s2, s3, "They are"))) 

print()
print()
print(f'Is s1 ends with "friend!"? {s1.endswith("friend!")}!')