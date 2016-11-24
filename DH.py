from User import *

p_bob = 15* "\t"
p_centr = 7*"\t"

def start_DH(point, p):
    print "Alice initializing ..."
    alice = User(p)
    print p_bob + "Bob initializing ..."
    bob = User(p)

    print p_centr + "Exchanging key ..."
    abP, baP = exchangeSecret_DH(point, alice, bob, True)

    print "Alice key: ", abP
    print "Bob key:   ", baP
    print

    if abP == baP:
        return 0, "Keys are equal, DH succeded !"
    else:
        return 1, "Diffre-Hellman failed."

def exchangeSecret_DH(point, alice, bob, _return = False):
    aP = alice.computePoint(point)
    bP = bob.computePoint(point)

    abP = alice.computePoint(bP)
    baP = bob.computePoint(aP)

    alice.addSharedSecret(abP)
    bob.addSharedSecret(baP)

    if _return:
        return abP, baP