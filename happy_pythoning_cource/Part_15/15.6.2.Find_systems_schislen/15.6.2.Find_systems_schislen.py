'''


В саду 88n​ фруктовых деревьев, из них 32n3​ яблони, 22n груши, 16n16_n16n​ слив и 17n вишен. В какой системе счисления посчитаны деревья?

Примечание. Переведите числа из nnn-ой системы счисления в десятичную и составьте уравнение.
'''

def trans_to_10(num, base=2):
    res = 0
    alp = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    
    for i in range(1, len(num)+1):
        if '0' <= num[-i] <= '9':
            res += int(num[-i]) * base**(i - 1)
        if num[-i].upper() in alp:
            #print(ord(num[-i]))
            n = ord(num[-i].upper()) - 55
            res += n * base**(i - 1)
            
    return res
    
#n = '11'
#print(trans_to_10(n, 2))
s1 = '88'
list_n = ['32', '22', '16', '17']
for base_sch in range(8,16):
    s = 0
    for n in list_n:
        s += trans_to_10(n, base_sch)
    s1 = trans_to_10('88', base_sch)
    if s1 == s:
        print(f'Использована {base_sch}-ная система счисления')