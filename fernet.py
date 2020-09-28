from cryptography.fernet import Fernet
import base64

# decisao 1
entrar = input('Deseja fazer login S/N : ')
if entrar == 'S' or entrar == 's':
    # entrada
    senha = input('Digite uma senha : ')

    # processamento
    key = Fernet.generate_key()  # geração de key Fernet
    cifra = Fernet(key)
    # encode para transformar a senha em base64
    senha_encode_64 = senha.encode('utf-8')
    # encriptacao da mensagem
    token = cifra.encrypt(senha_encode_64)
    # saida
    print('--------------------------------------------------------------------------------------------------------')
    print(token)
    print('--------------------------------------------------------------------------------------------------------')

    decripto = input('Deseja visualizar a senha descriptografada S/N : ')
    # decisao 2
    if decripto == 'S' or decripto == 's':
        # processamento
        decoded = cifra.decrypt(token)
        # saida
        print('--------------------------')
        print(decoded)
        print('--------------------------')
    else:
        print('Saindo...')
else:
    print('Saindo...')
