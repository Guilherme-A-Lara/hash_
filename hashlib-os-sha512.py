import hashlib
import os
'''
encode() : Converts the string into bytes to be acceptable by hash function.
digest() : Returns the encoded data in byte format.
hexdigest() : Returns the encoded data in hexadecimal format.
'''

entrar = input('Deseja fazer login S/N : ')
if entrar == 'S' or entrar == 's':
    user = input('Digite sua senha :')
    password_salt = os.urandom(32).hex()
    password = user

    hash = hashlib.sha512()
    hash.update(('%s%s' % (password_salt, password)).encode('utf-8'))
    password_hash = hash.hexdigest()
    senha = password_hash
    print('--------------------------------------------------------------------------------------------------------')
    print(senha)
    print('--------------------------------------------------------------------------------------------------------')
    ver = input('Deseja visualizar sua senha S/N : ')
    if ver == 'S' or ver == 's':
        print('--------------------------')
        print(f'Sua senha e : {user}')
        print('--------------------------')
    else:
        print('Saindo ...')
else:
    print('Saindo ...')
