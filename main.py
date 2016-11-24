from Curve import *
from DH import start_DH
from DSA import *
from Data import *
from User import *
from ElGammal import *
from STS import *
#
#### MAIN ####
#
center = 10*"\t"
print center  + "Opening file ..."
path = "/home/magali/PycharmProjects/EC/elliptic_curves/Weierstrass/"
folder = "cw512/"
file = "w512-001.gp"
file_path = path + folder + file
print center + file_path
#
print center + "Loading data ..."
data = Data(file_path)
c = Curve(data.p, data.n, data.a4, data.a6)
point = Point(data.gx, data.gy, c, False)
print center + "Data Loaded!"



print
raw_input(center + "Start the Diffre-Hellman key exchange ?")
dh_return, error_m = start_DH(point, data.p)
print center + error_m
#
#eg_succed = start_ElGammal(point, data.p, data.n, "Hello Bob")
#assert eg_succed == 0, center + "[ASSERT ERROR] El Gammal failed"
print center +  "El Gammal succeded !"

#dsa_succed = start_DSA(point, data.n, "Bonjour Bob, ici Alice")
#assert dsa_succed == 0, "[ASSERT ERROR] DSA failed"
print center + "DSA succeded !"

#sts_succed = start_STS(point, data.p, data.n)
#assert sts_succed == 0, "[ASSERT ERROR] STS failed"
print center +  "STS succeded !"

