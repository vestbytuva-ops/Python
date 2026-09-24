#trapesmetode
# from math import sqrt

# def f(x):
#     return sqrt(4 - x**2)

# a = -2
# b = 2
# n = 5
# dx = (b - a) / n
# areal = 0

# for i in range(n):
#     areal = areal + (f(dx * i + a) + f(dx*(i + 1) + a)) / 2 * dx

# print(areal)


#2.25
def f(x):
    return x**(2*x)

a = 1
b = 5
n = 20
dx = (b - a) / n
areal = 0

for i in range(n):
    areal = areal + f(dx * (i + 1 / 2) + a) * dx
print(areal)


