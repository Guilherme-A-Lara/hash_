import hashlib
'''
encode() : Converts the string into bytes to be acceptable by hash function.
digest() : Returns the encoded data in byte format.
hexdigest() : Returns the encoded data in hexadecimal format.
'''


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


entrar = input('Deseja fazer login S/N : ')
if entrar == 'S' or entrar == 's':
    # encriptação
    hash_string = input('Digite sua Senha: ')
    sha_signature = encrypt_string(hash_string)
    # saida do valor criptografado
    print('--------------------------------------------------------------------------------------------------------')
    print(sha_signature)
    print('--------------------------------------------------------------------------------------------------------')
    ver = input('Deseja visualizar sua senha S/N : ')
    if ver == 'S' or ver == 's':
        print('--------------------------')
        print(f'Sua senha é : {hash_string}')
        print('--------------------------')
    else:
        print('Saindo..')
else:
    print('Saindo...')
