from random import randint
from Utils import *
from Point import *
from User import *

def start_DSA(point, p, n, m_send):

    dsa = DSA(point, n)

    alice = User(n , m_send)
    bob = User(n, 0) #TODO change to str

    A = alice.generatePublicKey(point)
    u, v, m = dsa.sign(alice)

    nb, error_m = dsa.verify(A, m, u, v)
    if nb != 0:
        print error_m
    return nb



class DSA:
    def __init__(self,point, n):
        self.point = point
        self.n = n


    def sign(self, alice):
        k = randint(1, self.n-1)
        T = self.point.mul(k)
        x, y = T.x, T.y

        u = x % self.n
        v = ((H(alice.message) + alice.x*u) * invmodp(k, self.n)) % self.n

        if u == 0 or v == 0:
            return (self.sign(alice))
        else:
            return u, v, alice.message

    def verify(self, A, m, u, v):
        #  1 < u < n-1
        if u < 1 or u > self.n-1:
            return 1, "[DSA ERROR] VERIFICATION: u is not in the interval"
        # 1 < v < n-1
        elif v < 1 or v > self.n-1:
            return 1, "[DSA ERROR] VERIFICATION: v is not in the interval"
        # A != O
        elif A.inf:
            return 1, "[DSA ERROR] VERIFICATION: Alice public key is (0, 0) "
        # A belongs to C
        elif not(self.point.c.contains(A.x, A.y)):
            return 1, "[DSA ERROR] VERIFICATION: Alice public key is not on the curve "
        # nA = O
        elif not(A.mul(self.n).inf):
            return 1, "[DSA ERROR] VERIFICATION: A*n != 0 "
        else:
            tmp = (H(m)*invmodp(v, self.n)) % self.n
            T = self.point.mul(tmp)
            tmp = u*invmodp(v, self.n) % self.n
            T = T + A.mul(tmp)
            x = T.x
        # u = x%n
            if u != x%self.n :
                return 1, "[DSA ERROR] VERIFICATION: u != x%n"
            return 0, "[DSA] Verification OK"
