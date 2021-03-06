from DH import *
from AES import *
from DSA import *

p_bob = 15* "\t"
p_centr = 7*"\t"

def start_STS(point, p, n):
    sts = STS(point, p, n)

    print "Alice initializing ..."
    alice = User(p, "")
    A = alice.generatePublicKey(point)

    print p_bob + "Bob initializing ..."
    bob = User(p, "")
    B = bob.generatePublicKey(point)

    print p_centr + "Exchange shared secret ..."
    exchangeSecret_DH(point, alice, bob)

    print "Alice send cipher to Bob ..."
    a_cipher = sts.compute_cipher(alice, A, B)
    b_return, error_m = sts.verify_cipher(bob, a_cipher, B, A)
    print p_bob + error_m

    print p_bob + "Bob send cipher to Alice ..."
    b_cipher = sts.compute_cipher(bob, B, A)
    a_return, error_m = sts.verify_cipher(alice, b_cipher, A, B)
    print error_m

    return a_return + b_return

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

        return 0, "[STS] Verification OK, shared secret validated"






