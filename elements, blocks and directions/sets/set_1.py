# Множества.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(*basket)

print()

for x in basket:
	print('I love', x+'!')

y = 'grape'
print()
if y in basket:
	print(y,'in basket')
else:
	print(y,'not in basket')
