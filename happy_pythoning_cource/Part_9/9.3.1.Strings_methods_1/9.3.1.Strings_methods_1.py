'''
Strings methods 1
'''

s = 'i Learn Python language'
print(s.capitalize()) # I learn python language

s = 'i LEARN Python LAnguaGE'
print(s.lower()) # i learn python language

s = '$12344%^$#@!'
print(s.lower()) # $12344%^$#@!

s1 = 'a'
s2 = s1.upper()
print(s1, s2) # a A

s = 'i LEARN Python LAnguaGE'
print(s.upper()) # I LEARN PYTHON LANGUAGE

s = 'i LEARN Python LAnguaGE'
print(s.swapcase())