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
folder = "cw256/"
file = "w256-001.gp"
file_path = path + folder + file
print center + file_path
#
print center + "Loading data ..."
data = Data(file_path)
c = Curve(data.p, data.n, data.a4, data.a6)
point = Point(data.gx, data.gy, c, False)
print center + "Data Loaded!"



print
print center + "###########################################"
print center + "               Diffre-Hellman"
print center + "###########################################"

raw_input(center + "              Start ?")
dh_return, error_m = start_DH(point, data.p)
print center + error_m
#
print
print center + "###########################################"
print center + "               El Gammal"
print center + "###########################################"
raw_input(center + "              Start ?")
eg_return, error_m = start_ElGammal(point, data.p, "Hello Bob")
print center + error_m

print
print center + "###########################################"
print center + "                   DSA"
print center + "###########################################"
raw_input(center + "              Start ?")
dsa_return, error_m = start_DSA(point, data.n, "Bonjour Bob, ici Alice")
print center + error_m

print
print center + "###########################################"
print center + "                   DSA"
print center + "###########################################"
raw_input(center + "              STS ?")
sts_return = start_STS(point, data.p, data.n)


