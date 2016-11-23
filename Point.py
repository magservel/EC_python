from Utils import *
class Point:
    def __init__(self, x, y, c, inf):
        self.x = x % c.p
        self.y = y % c.p
        self.c = c
        self.inf = inf

    def __eq__(self, q):
        return self.x == q.x and self.y == q.y

    def __neg__(self):
        assert ((self.c.contains(self.x, (-self.y)%self.c.p))), \
            "C[POINT OPP ERROR]: Point initialise not on curve."

        return Point(self.x, (-self.y)%self.c.p, self.c, self.inf)

    def double (self):
        t = (3* pow(self.x, 2) + self.c.a4)*invmodp(2*self.y, self.c.p)
        x = (pow(t, 2) - self.x - self.x) % self.c.p
        y = (-(self.y + t * (x - self.x))) % self.c.p

        assert ((self.c.contains(x, y))), \
            "C[POINT DOUBLE ERROR]: Point initialise not on curve."
        return Point(x, y, self.c, self.inf)

    def add_distinct(self, q):
        d = self.x -q.x
        t = (self.y - q.y) % self.c.p * invmodp(d, self.c.p)
        x = (pow(t, 2) - self.x - q.x) % self.c.p
        y = (t * (self.x - x) - self.y) % self.c.p
        assert ( (self.c.contains(x, y))), \
                     "C[POINT ADD_D ERROR]: Point initialise not on curve."
        return Point(x, y, self.c, self.inf)

    def __add__ (self, q):
        if self.inf:
            return q
        if q.inf:
            return self
        if self == -q:
            return Point(0, 1, self.c, True)
        if self == q:
            return self.double()
        else:
            return self.add_distinct(q)

    def mul(self, k):
        k = k % self.c.p
        print
        if k < 0 :
            return -self.mul(-k)
        if k == 0:
            return Point(0, 1, self.c, True)

        else:
            q = self
            r = Point(0, 1, self.c, True)
            i = 1
            while i <= k:
                if k & i == i:
                    r = r + q
                i = i << 1
                q = q + q

        return r

