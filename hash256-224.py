import hashlib


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def decrypt_string(hash_string):
    sha_signature_decrypt = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature_decrypt


entrar = input('Deseja fazer login S/N : ')
if entrar == 'S' or entrar == 's':
    hash_string = input('Digite sua Senha: ')
    sha_signature = encrypt_string(hash_string)
    sha_signature_decrypt = decrypt_string(hash_string)
    print('Senha criptografada : ')
    print('--------------------------')
    print(sha_signature[:8])
    print('--------------------------')
    ver = input('Deseja ver a senha descriptografada S/N ')
    if ver == 'S' or ver == 's':
        print('--------------------------')
        print(f'Sua senha e : {hash_string}')
        print('--------------------------')
    else:
        print('Saindo ...')
else:
    print('Saindo ...')
