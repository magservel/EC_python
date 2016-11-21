
def invmodp(a, p):
    '''
    The multiplicitive inverse of a in the integers modulo p.
    Return b s.t.
    a * b == 1 mod p
    '''

    for d in xrange(1, p):
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d
