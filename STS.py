from DH import *
from AES import *
from DSA import *

def start_STS(point, p, n):
    sts = STS(point, p, n)

    alice = User(p, "")
    bob = User(p, "")

    A = alice.generatePublicKey(point)
    B = bob.generatePublicKey(point)

    exchangeSecret_DH(point, alice, bob)

    print "Alice send cipher to Bob ..."
    a_cipher = sts.compute_cipher(alice, A, B)
    b_return, error_m = sts.verify_cipher(bob, a_cipher, B, A)
    print error_m

    print "Bob send cipher to Alice ..."
    b_cipher = sts.compute_cipher(bob, B, A)
    a_return, error_m = sts.verify_cipher(alice, b_cipher, A, B)
    print error_m

    return a_return and b_return

class STS:
    def __init__(self, point, p, n):
        self.point = point
        self.p = p
        self.n = n

    def conc(self, A, B):
        return str(A.x) + '||' + str (B.x)

    def compute_cipher (self, user, X, Y):
        C = self.conc(X, Y)

        dsa = DSA(self.point, self.n)
        u, v, m = dsa.sign(user, C)

        D = str(u) + '$' + str(v) + '$' + str(m)
        u_cipher =  encrypt_AES(user, D)

        return u_cipher

    def verify_cipher (self, user, cipher, X, Y):
        D = decrypt_AES(user, cipher)
        [u, v, C] = D.split('$')

        u = int(u)
        v = int(v)
        if C != self.conc(Y, X):
            return 1, "[STS ERROR] Received message is different from expected"



        dsa = DSA(self.point, self.n)
        nb, error_m = dsa.verify(Y, C, u, v)
        if nb != 0:
            return nb, error_m

        return 0, "[STS] Verification OK"






