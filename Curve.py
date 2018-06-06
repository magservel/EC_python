class Curve(object):
    def __init__(self, p, n, a4, a6):
        self.p = p
        self.n = n
        self.a4 = a4
        self.a6 = a6

    def contains(self, x, y):
        return (y*y - x*x*x-self.a4*x - self.a6) % self.p == 0