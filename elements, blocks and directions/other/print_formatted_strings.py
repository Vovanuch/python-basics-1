''' formatted strings features'''
h = 5
m = 2
n = 12

print('Your time is', "%02d:%02d:%02d" % (h, m, n))




ip = '192.168.0.1'
mask = 24
octets = ['192', '168', '0', '1']
octets2 = [192, 168, 0, 1]

# Выполнение функций внутри f-строки
print(f"IP: {'.'.join(octets)}, mask: {mask}")

#print(f"IP: {oc for oc in octets2}, mask: {mask}")


# Большааааая строка
oc1, oc2, oc3, oc4 = [192, 168, 0, 1]
print(f'''
        ...: IP-address is:
        ...: {oc1:<8}     {oc2:<8}      {oc3:<8}      {oc4:<8}
        ...: {oc1:<08b}     {oc2:<08b}      {oc3:<08b}      {oc4:<08b}
        ...: mask is {mask}
        '''
        )

# Работаем с f-строками в цикле
lst_ip_addresses = ['192.168.1.1/24', '10.10.1.1/8', '255.255.255.254/31']
for ip_address in lst_ip_addresses:
    ip, mask = ip_address.split('/')
    print(f'ip: {ip}, mask: {mask}')


