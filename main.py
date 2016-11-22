from Data import *
from Curve import *
from Point import *
from Utils import invmodp
from DH import *
from ElGammal import *




path = "/home/magali/PycharmProjects/EC/elliptic_curves/Weierstrass/"
folder = "cw256/"
file = "w256-001.gp"
file_path = path + folder + file
print file_path

data = Data(file_path)
c = Curve(data.p, data.n, data.a4, data.a6)
p = Point(data.gx, data.gy, c, False)


#print p.double()
#dh = DH(p)
#dh.start()
eg = ElGammal(data.p, data.n)
eg.alice.message = 6678637864379369236946747684687684
eg.start()

