from Curve import *
from DH import *
from DSA import *
from Data import *
from User import *
from ElGammal import *
#
#### MAIN ####
#
path = "/home/magali/PycharmProjects/EC/elliptic_curves/Weierstrass/"
folder = "cw256/"
file = "w256-001.gp"
file_path = path + folder + file
print file_path

data = Data(file_path)
c = Curve(data.p, data.n, data.a4, data.a6)
point = Point(data.gx, data.gy, c, False)

dh_succed = start_DH(point, data.p, data.n)
assert dh_succed == 0, "Diffre-Hellman failed"
print"DH succeded !"

eg_succed = start_ElGammal(point, data.p, data.n, 123456778) #TODO change to a str
assert eg_succed == 0, "El Gammal failed"
print "El Gammal succeded !"

dsa_succed = start_DSA(point, data.p, data.n, "Bonjour Bob, ici Alice")
assert dsa_succed == 0, "DSA failed"
print "DSA succeded !"

#eg = ElGammal(data.p, point)
#eg.alice.message = 7643876387658787465874682684654794659746492
#eg.start()

#dsa = DSA(data.n, point)
#dsa.alice.message = "Bonjour Bob, c'est Alice"
#dsa.start()

#sts = STS()

#print binascii.crc32("hello world")
# Or, in two pieces:
#crc = binascii.crc32("hello")
#crc = binascii.crc32(" world", crc) & 0xffffffff
#print 'crc32 = 0x%08x' % crc