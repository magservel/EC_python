
class Curve:
    def __init__(self, p, n, a4, a6):
        self.p = p
        self.n = n
        self.a4 = a4
        self.a6 = a6

    def contains(self, x, y):
        return (pow(y, 2) - pow(x, 3)-self.a4*x - self.a6) % self.p == 0