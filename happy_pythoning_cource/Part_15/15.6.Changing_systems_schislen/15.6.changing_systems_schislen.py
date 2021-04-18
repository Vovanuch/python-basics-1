'''
Переведите число в десятичную систему счисления.
'''
#s1 = '1AF2'



alp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

print('Введите исходное число:')
num = input().strip()
print('Введите систему счисления этого числа:')
system_schisl_base = int(input().strip())
res = 0
system_schisl_new = 10

for i in range(1, len(num)+1):
    if '0' <= num[-i] <= '9':
        res += int(num[-i]) * system_schisl_base**(i - 1)
    if num[-i].upper() in alp:
        #print(ord(num[-i]))
        n = ord(num[-i].upper()) - 55
        res += n * system_schisl_base**(i - 1)

print(res)