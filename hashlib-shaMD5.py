import hashlib
'''
encode() : Converts the string into bytes to be acceptable by hash function.
digest() : Returns the encoded data in byte format.
hexdigest() : Returns the encoded data in hexadecimal format.
'''
entrar = input('Deseja fazer login S/N : ')
if entrar == 'S' or entrar == 's':
    senha = input('Digite a sua senha: ')
    result = hashlib.md5(senha.encode())
    print(result.hexdigest())
    ver = input('Deseja visualizar sua senha S/N : ')
    if ver == 'S' or ver == 's':
        print(f'Sua senha é : {senha}')
    else:
        print('Saindo..')
else:
    print('Saindo...')
