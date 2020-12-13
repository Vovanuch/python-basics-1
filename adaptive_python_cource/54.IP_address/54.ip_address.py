'''


In the internet, each computer is assigned a four-byte code (IP address), which is usually written as four numbers, each of which can take the values from 0 to 255, separated by periods. Below are the examples of the correct IP addresses:
127.0.0.0
192.168.0.1
255.0.255.255

Write a program to determine whether the specified string is a correct IP address.

The program should take a string of arbitrary characters as input. If this string is a correct record of an IP address - output YES, otherwise - output NO.

Note

In order to convert string to number it is convenient to use the int function, which takes one string as an argument and returns a number.

Sample Input:

127.0.0.1

Sample Output:

YES

'''

def in_range_ip(n):
    if n in range(0,256):
        return True
    else:
        return False

try:
    list_octets = input().strip().split(sep='.')
    list_octets_int = [int(i) for i in list_octets]
    is_IP = False
    if len(list_octets_int) == 4:
        if in_range_ip(list_octets_int[0]):
            if in_range_ip(list_octets_int[1]):
                if in_range_ip(list_octets_int[2]):
                    if in_range_ip(list_octets_int[3]):
                        is_IP = True
                        #print("YES")
    if is_IP:
        print("YES")
    else:
        print("NO")
    
    '''    is_IP = False
    else:
        for i in list_octets_int:
        #print(f'octet is {i}')
            if in_range_ip(i) == False:
                is_IP = False
                print("NO")
                break
    if is_IP:
        print("YES")
    else:
        print("NO")'''
except:
    print("NO")