from hashlib import sha256

def invmodp(k, p):
    '''
    The multiplicitive inverse of a in the integers modulo p.
    Return b s.t.
    a * b == 1 mod p
    '''
    if k == 0:
        raise ZeroDivisionError('division by zero')

    if k < 0:
        # k ** -1 = p - (-k) ** -1  (mod p)
        return p - invmodp(-k, p)

    # Extended Euclidean algorithm
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t

    assert gcd == 1, "Modular doesn't exist"
    assert (k * x) % p == 1

    return x % p

def H(m):
    h = sha256(m)
    h = h.hexdigest()
    n = int(h, base=16)
    return n


def to_int(s):
    number = 0
    for e in [ord(c) for c in s]:
        number = (number * 0x110000) + e
    return number

def to_str(number):
    l = []
    while(number != 0):
        l.append(chr(number % 0x110000))
        number = number // 0x110000
    return ''.join(reversed(l))

def formated_string(x, size):
    while len(x) < size*8:
        x = '0' + x
    return x

def lenMod16(m):
    while (len(m) % 16 != 0):
        m = '0' + m
    return m


