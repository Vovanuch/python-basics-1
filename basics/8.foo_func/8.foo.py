''' foo function  '''

a = []

def foo(arg1, arg2):
    a.append("foo")

foo(a.append("arg1"), a.append("arg2"))

print(a)
# веведется ['arg1', 'arg2', 'foo']
