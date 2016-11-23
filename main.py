import binascii

from Data import *
from Curve import *
from Point import *
from DH import *
from ElGammal import *
from DSA import *
from STS import *

from Utils import *




path = "/home/magali/PycharmProjects/EC/elliptic_curves/Weierstrass/"
folder = "cw256/"
file = "w256-005.gp"
file_path = path + folder + file
print file_path

data = Data(file_path)
c = Curve(data.p, data.n, data.a4, data.a6)
point = Point(data.gx, data.gy, c, False)

dh = DH(point)
dh.start()

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


