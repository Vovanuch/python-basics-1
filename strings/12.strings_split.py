#12. Как разделить строку по заданному символу?

#Здесь нам поможет метод split(), который разбивает строку по заданному символу или по нескольким символам.

m1 = 'Very good string'.split(' ')
print(m1)
#=> ['Very', 'good', 'string']
m2 = 'Even--more--great'.split('--')
print(m2)
#=> ['Even', 'more', 'great']
