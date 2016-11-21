from Data import *
from Curve import *
from Point import *
from Utils import *
from DH import *




path = "/home/magali/PycharmProjects/EC/elliptic_curves/Weierstrass/"
folder = "cw256/"
file = "w256-001.gp"
file_path = path + folder + file
print file_path

data = Data(file_path)
c = Curve(data.p, data.n, data.a4, data.a6)
p = Point(data.gx, data.gy, c, False)

dh = DH(p)
p = p.double()
p = p.mul(4)
dh.start()
