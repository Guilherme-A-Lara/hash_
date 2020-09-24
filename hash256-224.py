import hashlib
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
def decrypt_string(hash_string):
    sha_signature_decrypt = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature_decrypt
hash_string = input('Digite sua Senha: ')
sha_signature = encrypt_string(hash_string)
sha_signature_decrypt = decrypt_string(hash_string)
print(sha_signature)
print(sha_signature_decrypt)