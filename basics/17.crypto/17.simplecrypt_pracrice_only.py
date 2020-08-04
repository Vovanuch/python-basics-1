''' using simplecrypt module. install it first!

pip3 install pycryptodome

pip3 install --no-deps simple-crypt

 '''

import simplecrypt
from simplecrypt import encrypt, decrypt


def get_decrypted_text(password, text):
    ''' try to find decrypted text '''
    try:
        result = decrypt(password, text)
    except simplecrypt.DecryptionException:
        print("Sorry, I cant do decryption. Wrong password or file.")
    else: 
        print('Result of decryption is', result)
        
         


text = input("Please, enter your text for encryption: ")
password = input("Please, enter strong password: ")
encrypted_file_name = input("What is the name of file where you want to write result? ")

encrypted_text_data = encrypt(password, text)

with open(encrypted_file_name, "wb") as out:
    out.write(encrypted_text_data)

wish = input("Do you want to read encrypted file? Yes or No: ")

if wish.lower() == 'yes':
    
    pass2 = input("Please, enter your password: ")
    with open(encrypted_file_name, "rb") as inf:
        encrypted_text_data = inf.read()
    get_decrypted_text(pass2, encrypted_text_data)
    
    
else:
    print("Ok, bye!")
