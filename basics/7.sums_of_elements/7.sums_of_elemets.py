''' sums of 2 and in list  '''
def sum_list(lst):
	result = 0
	for x in lst:
		result += x
	return result
	
def sum_two(arg1, arg2):
	return arg1 + arg2



print(sum_list([1, 2, 3]))
print(sum_two(2, 5))
