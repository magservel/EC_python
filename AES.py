from hashlib import sha256
from Utils import lenMod16
from Crypto.Cipher import AES

def getAESKey(user):
    K = bin(user.K.x)
    K = sha256(K.encode()).digest()
    return str(K)


def encrypt_AES(user, message):
    message = lenMod16(message)
    K = getAESKey(user)
    aes = AES.new(K)
    return aes.encrypt(message)


def decrypt_AES(user, ciphertext):
    K = getAESKey(user)
    aes = AES.new(K)
    return aes.decrypt(ciphertext)



