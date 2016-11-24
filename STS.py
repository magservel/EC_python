from User import User
from DH import *
from AES import *
from DSA import *

def start_STS(point, p, n):
    sts = STS(point, p, n)

    alice = User(p, "")
    bob = User(p, "")

    A = alice.generatePublicKey(point)
    B = alice.generatePublicKey(point)

    exchangeSecret_DH(point, alice, bob)

    a_cipher = sts.compute_cipher(alice, A, B)
    b_cipher = sts.compute_cipher(bob, B, A)








class STS:
    def __init__(self, point, p, n):
        self.point = point
        self.p = p
        self.n = n

    def conc(self, A, B):
        return str(A) + '$' + str (B)

    def compute_cipher (self, user, X, Y):
        C = self.conc(X, Y)

        dsa = DSA(self.point, self.n)
        u, v, m = dsa.sign(user, C)

        D = str(u) + '$' + str(v) + '$' + str(m)
        u_cipher =  encrypt_AES(user, D)

        return u_cipher

    def verify_cipher (self, user, cipher, X, Y): #TODO verify_cipher
        return 0






