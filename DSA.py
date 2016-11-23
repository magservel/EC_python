from random import randint
from Utils import *
from Point import *

class DSA:
    def __init__(self, n, point):
        self.n = n
        self.point = point

        self.alice = User(n)
        self.bob = User(n)

    def start(self):
        self.A = self.alice.generatePublicKey(self.point)
        u, v, m = self.alice.sign(self.n, self.point)
        self.bob.verify(self.n, self.point, u, v, self.A, m)



class User:
    def __init__(self, n):
        self.x = randint(1, n-1)
        self.message = 1234

    def generatePublicKey(self, g):
        self.X = g.mul(self.x)
        assert g.c.contains(self.X.x, self.X.y), \
            "[DSA ERROR] Generate public key failed"
        return self.X

    def sign(self, n, point):
        k = randint(1, n-1)
        T = point.mul(k)
        x, y = T.x, T.y

        u = x %n
        v = ((H(self.message) + self.x*u) * invmodp(k, n)) % n

        if u == 0 or v == 0:
            return (self.sign(n, point))
        else:
            return u, v, self.message

    def verify(self, n, point, u, v, A, m):
        #  1 < u < n-1
        if u < 1 or u > n-1:
            print "[DSA ERROR] VERIFICATION: u is not in the interval"
            return
        # 1 < v < n-1
        elif v < 1 or v > n-1:
            print "[DSA ERROR] VERIFICATION: v is not in the interval"
            return
        # A != O
        elif A.inf:
            print "[DSA ERROR] VERIFICATION: Alice public key is (0, 0) "
            return
        # A belongs to C
        elif not(point.c.contains(A.x, A.y)):
            print "[DSA ERROR] VERIFICATION: Alice public key is not on the curve "
            return
        # nA = O
        elif not(A.mul(n).inf):
            print "[DSA ERROR] VERIFICATION: A*n != 0 "
            return
        else:
            tmp = (H(m)*invmodp(v, n)) % n
            T = point.mul(tmp)
            tmp = u*invmodp(v, n) % n
            T = T + A.mul(tmp)
            x = T.x
        # u = x%n
            if u != x%n :
                print "[DSA ERROR] VERIFICATION: u != x%n"
                return
            print "[DSA] Verification OK"
