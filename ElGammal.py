from random import randint
from Utils import *
from Point import *
from User import *

def start_ElGammal(point, p, n, m_send):

    eg = ElGammal(point, p)

    alice = User(p, m_send)
    bob = User(p, 0) #TODO change to str

    A = alice.generatePublicKey(point)
    B = bob.generatePublicKey(point)

    c1, c2 = eg.encode(alice, B)
    m_received = eg.decode(bob, c1, c2)

    if m_send == m_received:
        return 0
    else:
        return 1


class ElGammal:
    def __init__(self, point, p):
        self.point = point
        self.p = p

    def encode(self, alice, B):
        c1 = to_int(alice.message)+ B.mul(alice.x).x
        c2 = alice.generatePublicKey(self.point)
        return c1, c2

    def decode(self, bob, c1, c2):
        m = (c1 - c2.mul(bob.x).x) % self.p
        bob.message = to_str(m)
        return bob.message