'''  function_name, type. function name is also an object! '''
def function_name(arg1, arg2):
    return (arg1 + arg2)
x = function_name(2, 11)
y = function_name(x, 6)
print('x = ', x)
print('y = ', y)
print(type(function_name)) # class <function>
print('id of function_name is', id(function_name))
print(type(type(3)))
