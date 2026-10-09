def f(x):
    return x**3-4*x

areal = 0
a = -2
b = 0
n = 8
dx = (b-a)/n

for i in range(n):
    x = a+dx*i
    areal = areal + f(x)*dx
print(areal)