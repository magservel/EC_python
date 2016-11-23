from Crypto.Cipher import AES

class STS:
    def __init__(self):
        print "HELLO STS"
        obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
        message = "The answer is no"
        ciphertext = obj.encrypt(message)
        print ciphertext
