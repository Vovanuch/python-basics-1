'''
strings format
'''

sentence = 'Moscow is the capital of Russia'
template = '{} is the capital of {}'

print(sentence)
print(template.format("Minsk", "Resp.Belarus'"))
print(template.format("Tegeran", "Iran"))

#print(str.format.__doc__)

# directly change the order of arguments 
print()
print('directly change the order of arguments ')
template2 = '{1} is the capital of {0}'
print(template2.format("Iraq", "Bagdad"))

# named arguments
print()
print('named arguments')
template3 = '{capital} is the capital of {country}'
print(template3.format(country="Iraq", capital="Bagdad"))
print(template3.format(capital="Deli", country="India"))
