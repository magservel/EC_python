from random import randint
from Utils import *
from Point import *

class ElGammal:
    def __init__(self, p, g):
        self.p = p
        self.g = g
        self.bob = User(p)
        self.alice = User(p)

    def start(self):
        print "Public Key Construction"
        self.B = self.bob.generatePublicKey(self.g)
        print "B : ", self.B
        self.A = self.alice.generatePublicKey(self.g)
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
        self.message = 1234

    def generatePublicKey(self, g):
        self.X = g.mul(self.x)
        # self.X = pow(g, self.x, p)
        return self.X


    def encode(self, B, p):
        c1 = hash(self.message)+ B.mul(self.x).x
        # c1 = (self.message * pow(B, self.x, p)) % p
        c2 = self.X
        return c1, c2

    def decode(self, c1, c2, p):
        m = (c1 - c2.mul(self.x).x) %p
        #r1 = pow(c1, self.x, p)
        #r1 = invmodp(r1, p)
        #m = (c2 * r1) %p
        self.message = unhash(m)