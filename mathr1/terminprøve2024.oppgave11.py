from pylab import *

OA = array([1,8])
OB = array([4,3])

OM = (OA+OB)/2
AB = OB-OA

v = array([AB[1], -AB[0]])
s = 0
OC = array(OM + s*v)
