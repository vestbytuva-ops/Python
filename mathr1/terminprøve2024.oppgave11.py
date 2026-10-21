from pylab import *

OA = array([1,8])
OB = array([4,3])

OM = (OA+OB)/2
AB = OB-OA

v = array([AB[1], -AB[0]])
s = 0
OC = array(OM + s*v)

while sum((OC-OA)**2)**0.5 < sum((OB-OA)**2)**0.5:
    s = s+0.001
    OC = array(OM+s*v)

print(OC)