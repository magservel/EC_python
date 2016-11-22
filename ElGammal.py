from random import randint
from Utils import *

class ElGammal:
    def __init__(self, p, n):
        self.p = p
        self.g = p/2 - 1
        self.bob = User(p)
        self.alice = User(p)

    def start(self):
        print "Public Key Construction"
        self.B = self.bob.generatePublicKey(self.g, self.p)
        print "B : ", self.B
        self.A = self.alice.generatePublicKey(self.g, self.p)
        print "A : ", self.A


        print "Encode message exchange"
        (C1, C2) = self.alice.encode(self.B, self.p)

        print "Alice sends ", self.alice.message
        print "C1 = ",C1
        print "C2 = ", C2

        self.bob.decode(C1, C2, self.p)
        print "Bob decodes : ", self.bob.message


        if self.alice.message == self.bob.message:
            print "The communication succeded !"
        else:
            print "The communication failed"




class User:
    def __init__(self, p):
        self.x = randint(1, p-1)

    def generatePublicKey (self, g, p):
        self.X = pow(g, self.x, p)
        return self.X


    def encode(self, B, p):
        c1 = self.X
        c2 = (self.message * pow(B, self.x, p)) % p
        return c1, c2

    def decode(self, c1, c2, p):
        r1 = pow(c1, self.x, p)
        r1 = invmodp(r1, p)
        m = (c2 * r1) %p
        self.message = m