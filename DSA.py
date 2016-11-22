from random import randint
from Utils import *
from Point import *

class DSA:
    def __init__(self, p, point):
        self.p = p
        self.point = point

        self.alice = User(p)
        self.bob = User(p)

    def start(self):
        self.A = self.alice.generatePublicKey(self.point)
        u, v = self.alice.sign(self.p, self.point)
        self.bob.verify(self.p, self.point, u, v, self.A)



class User:
    def __init__(self, p):
        self.x = randint(1, p-1)
        self.message = 1234

    def generatePublicKey(self, g):
        self.X = g.mul(self.x)
        return self.X

    def sign(self, p, point):
        k = randint(1, p-1)
        T = point.mul(k)
        x, y = T.x, T.y
        u = x %p
        v = ((hash(self.message) + self.x*u) * invmodp(k, p)) % p

        if u == 0 or v == 0:
            return (self.sign(p, point))
        else:
            return u, v

    def verify(self, p, point, u, v, A):
        if u < 1 or u > p-1:
            print "[DSA ERROR] VERIFICATION: u is not in the interval"
            return
        elif v < 1 or v > p-1:
            print "[DSA ERROR] VERIFICATION: v is not in the interval"
            return
        #elif u != x %p: #TODO: u = x%p
        #    print "[DSA ERROR] VERIFICATION: u != x%p"
        #    return
        elif A.inf:
            print "[DSA ERROR] VERIFICATION: Alice public key is (0, 0) "
            return
        elif not(point.c.contains(A.x, A.y)):
            print "[DSA ERROR] VERIFICATION: Alice public key is not on the curve "
            return
        elif not(A.mul(p).inf):
            print "[DSA ERROR] VERIFICATION: A*p != 0 "
            return
        else:
            print "[DSA] Verification OK"
