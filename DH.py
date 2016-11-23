from User import *

def start_DH(point, p, n):
    alice = User(p, "No message")
    bob = User(p, "No message")

    aP = alice.computePoint(point)
    bP = bob.computePoint(point)

    abP = alice.computePoint(bP)
    baP = bob.computePoint(aP)

    if abP == baP:
        return 0
    else:
        return 1