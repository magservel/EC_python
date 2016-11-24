from random import randint
from Utils import *
from Point import *
from User import *

p_bob = 20* "\t"
p_centr = 10*"\t"

def start_ElGammal(point, p, m_send):

    eg = ElGammal(point, p)

    print "Alice initializing ..."
    alice = User(p, m_send)
    A = alice.generatePublicKey(point)

    print p_bob + "Bob initializing ..."
    bob = User(p)
    B = bob.generatePublicKey(point)


    print "Alice sends: " + m_send
    c1, c2 = eg.encode(alice, A, B)
    print "encrypted as "
    print "   C1: " + str(c1)
    print " C2.x: " + str(c2.x)
    print " C2.y: " + str(c2.y)
    m_received = eg.decode(bob, c1, c2)
    print p_bob + "Bob decryptes: " + m_received

    if m_send == m_received:
        return 0, "El Gammal ended correctly."
    else:
        return 1, "El Gammal failed."


class ElGammal:
    def __init__(self, point, p):
        self.point = point
        self.p = p

    def encode(self, alice, A, B):
        c1 = to_int(alice.message)+ B.mul(alice.x).x
        c2 = A
        return c1, c2

    def decode(self, bob, c1, c2):
        m = (c1 - c2.mul(bob.x).x) % self.p
        bob.message = to_str(m)
        return bob.message