#
#
#
#
from random import randint


class DH:
    def __init__(self, point):
        self.point = point
        print "Alice key is "
        self.alice = User(point.c.p)
        print "Bob key is"
        self.bob = User(point.c.p)

    def start(self):
        self.aP = self.alice.computeP(self.point)
        self.bP = self.bob.computeP(self.point)

        self.abP = self.alice.computeP(self.bP)
        self.baP = self.bob.computeP(self.aP)

        if self.abP == self.baP:
            print "Key Exchange is a succes !"
        else:
            print "Key Exchange failed."


class User:
    def __init__(self, p):
        self.m = randint(1, p - 1)
        print self.m

    def computeP(self, point):
        return
