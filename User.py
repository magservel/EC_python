from Point import *
from random import randint

class User:
    def __init__(self, p, m = ""):
        self.x = randint(1, p-1)
        self.message = m

    def generatePublicKey(self, point):
        X = point.mul(self.x)
        assert point.c.contains(X.x, X.y), "Public key generation failed"
        return X

    def computePoint(self, point):
        return point.mul(self.x)

    def addSharedSecret(self, K):
        self.K = K