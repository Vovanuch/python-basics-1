''' using simplecrypt module. install it first!

pip3 install pycryptodome

pip3 install --no-deps simple-crypt

 '''

import simplecrypt
from simplecrypt import encrypt, decrypt

str_encrypted = ''
str_decrypted = ''
passwords = []
lst_str_decrypted = []


def get_str_decrypted_result(password, string, original_string):
    ''' try to find decrypted text '''
    try:
        result = decrypt(password, string)
    except simplecrypt.DecryptionException:
        print(f"{password} is bad password")
    else:
        print("The answer is:")
        print(f'{result}')
        original_string = result
        return result
    finally:
        print("Try next?")
    


with open("encrypted.bin", 'rb') as file_input:
    str_encrypted = file_input.read()
    

    
with open("passwords.txt", 'r') as files_passwds:
    passwords = files_passwds.readlines()

passwords = [x.strip() for x in passwords]



for p in passwords:
    get_str_decrypted_result(p, str_encrypted, str_decrypted)

print(str_decrypted) 
