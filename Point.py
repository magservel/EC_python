from Curve import *
from Utils import *
class Point:
    def __init__(self, x, y, c, inf):
        # type: (object, object, object, object) -> object
        self.x = x
        self.y = y
        self.c = c
        self.inf = inf

        if not(self.c.contains(x, y)):
            print "[POINT ERROR]: Point initialise not on curve."

    def __eq__(self, q):
        return self.x == q.x and self.y == q.y

    def opp(self):
        return Point(self.x, (self.x + self.y)%self.c.p, self.c, self.inf)

    def double (self):
        t = (3* pow(self.x, 2) + self.a4*invmodp(2*self.y, self.c.p))
        x = (pow(t, 2) - self.x - self.x) % self.c.p
        y = -(self.y + t * (x - self.x)) % self.c.p
        return Point(x, y, self.c.p, self.inf)

    def add_distinct(self, q):
        d = self.x -q.x
        t = (self.y - q.y) % p * invmodp(d, self.c.p)
        x = (pow(t, 2) - self.x - q.x) % self.c.p
        y = (t * (self.tx - x) - self.y) % self.c.p
        return Point(x, y, self.c, self.inf)

    def __add__ (self, q):
        if self.inf:
            return q
        if q.inf:
            return self
        if self == q.opp():
            return Point(0, 1, self.c, True)
        if self == q:
            return self.double()
        else:
            return self.add_distinct(q)

    def mul(self, k):
        if k % self.c.p == 0:
            return Point(0, 1, True)
        if k < 0:
            return self.opp().mul(-k)
        k = bin(k)
        k = k[2:]
        r = Point(0, 1, self.c, True)
        for b in k:
            r = r.double()
            if b == '1':
                r = r.add(self)
        return r

