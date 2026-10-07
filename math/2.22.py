from math import sqrt as s

def f(x):
    return s(4-x**2)

a=-2
b=2
n=10

dx = (b-a)/n
areal = 0

for i in range(n):
    areal1 += areal + f(dx*i+a)*dx #venstremetode
    areal2 += areal + f(dx*(i+1)+a)*dx #høyremetode

print("Dette er venstremetode {areal1}, dette er høyremetode {areal2}")

