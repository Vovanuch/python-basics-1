'''  default args '''

def s(a, *args, b=10):
    print('a=', a)
    res = a + b
    for v in args:
        print('v=', v)
        res += v
    print('b=', b)
    return res

        
    


print('s(11, 10, b=10) =', s(11, 10, b=10))
print('s(0, 0, 31) =', s(0, 0, 31))
#print('s(b=31, 0)', s(b=31, 0))
print('s(21)', s(21))
print('s(11, 10, 10) =', s(11, 10, 10))
#print('s(b=31)', s(b=31))
print('s(5, 5, 5, 5, 1) =', s(5, 5, 5, 5, 1))
print('s(11, b=20) =', s(11, b=20))
print('s(11, 10) =', s(11, 10))
