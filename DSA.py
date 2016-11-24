from User import *

p_bob = 20* "\t"
p_centr = 10*"\t"

def start_DSA(point, n, m_send):

    dsa = DSA(point, n)
    print "Alice initializing ..."
    alice = User(n , m_send)

    A = alice.generatePublicKey(point)
    print "Alice signs: " + m_send

    u, v, m = dsa.sign(alice)
    print "with "
    print " u: " + str(u)
    print " v: " + str(v)
    print " m: " + str(m)

    print p_bob + "Verification ..."
    nb, error_m = dsa.verify(A, m, u, v)

    return nb, error_m

class DSA:
    def __init__(self,point, n):
        self.point = point
        self.n = n

    def sign(self, user, m = ""):
        # type: (User, str) -> int, int, str

        # Get (x, y) = k.Point (with 1 < k < n-1)
        k = randint(1, self.n-1)
        T = self.point.mul(k)
        x, y = T.x, T.y

        # Compute (u, v)
        if m == "":
            m = user.message
        u = x % self.n
        v = ((H(m) + user.x*u) * invmodp(k, self.n)) % self.n

        # Check that u and v != 0
        if u == 0 or v == 0:
            return (self.sign(user, m))
        else:
            return u, v, m

    def verify(self, A, m, u, v):
        #  1 < u < n-1
        if u < 1 or u > self.n-1:
            return 1, "[DSA ERROR] VERIFICATION: u is not in the interval"
        # 1 < v < n-1
        elif v < 1 or v > self.n-1:
            return 1, "[DSA ERROR] VERIFICATION: v is not in the interval"
        # A != O
        elif A.inf:
            return 1, "[DSA ERROR] VERIFICATION: Alice public key is (0, 0) "
        # A belongs to C
        elif not(self.point.c.contains(A.x, A.y)):
            return 1, "[DSA ERROR] VERIFICATION: Alice public key is not on the curve "
        # nA = O
        elif not(A.mul(self.n).inf):
            return 1, "[DSA ERROR] VERIFICATION: A*n != 0 "
        else:
            tmp = (H(m)*invmodp(v, self.n)) % self.n
            T = self.point.mul(tmp)
            tmp = u*invmodp(v, self.n) % self.n
            T = T + A.mul(tmp)
            x = T.x
        # u = x%n
            if u != x%self.n :
                return 1, "[DSA ERROR] VERIFICATION: u != x%n"
            return 0, "[DSA] Verification OK, no usurpation detected"
