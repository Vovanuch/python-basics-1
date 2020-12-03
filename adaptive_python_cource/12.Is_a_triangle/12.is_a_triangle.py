'''
Triangle

Given three natural numbers A, B, C. Define if the triangle with such sides exists.

If the triangle exists - output the YES string, otherwise - output NO.

Triangle is a three points that are not located on a single straight line.
'''
str_hello = 'Please, enter three natural numbers A, B, C. We will check, can they be a triangle sides, or not.'
print(str_hello)

str_error_1 = 'You enter incorrect values.'
a, b, c = input().strip(), input().strip(), input().strip()

try:
    a = float(a)
    b = float(b)
    c = float(c)
    
    res = ''
    
    if ((a + b) <= c) or ((a + c) <= b) or ((b + c) <= a):
        res = 'NO'
    else:
        res = 'YES'
    
    print(res)
    
except:
    print(str_error_1)