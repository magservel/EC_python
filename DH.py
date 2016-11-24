from User import *

def start_DH(point, p):
    alice = User(p, "No message")
    bob = User(p, "No message")

    abP, baP = exchangeSecret_DH(point, alice, bob, True)

    if abP == baP:
        return 0
    else:
        return 1

def exchangeSecret_DH(point, alice, bob, _return = False):
    aP = alice.computePoint(point)
    bP = bob.computePoint(point)

    abP = alice.computePoint(bP)
    baP = bob.computePoint(aP)

    alice.addSharedSecret(abP)
    bob.addSharedSecret(baP)

    if _return:
        return abP, baP