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
#a
# def f(x):
#     return x**(2*x)

# a = 1
# b = 5
# n = 20
# dx = (b - a) / n
# areal = 0

# for i in range(n):
#     areal = areal + f(dx * (i + 1 / 2) + a) * dx
# print(areal)

#b
# def f(x):
#     return x**(2*x)

# a=1
# b=5
# n=20
# areal=0

# dx = (b - a)/n

# for i in range(n):
#     areal = areal + f(dx * i + a) * dx

# print(areal)

# def f(x):
#     return x**(2*x)

# a=1
# b=5
# n=20
# areal=0

# dx = (b - a)/n

# for i in range(n):
#     areal = areal + f(dx * (i + 1) + a) * dx

# print(areal)


#2.26


a = 2
b = 1
n = 5

def f(x):
    return 1/(x*x**2)

def trapes_metode(a,b,n):
    dx = (b-a)/n
    areal = 0

    for i in range(n):
        x1 = a + i * dx
        x2 = a + (i+1) * dx
        areal = areal + (f(x1)-f(x2))/ 2 * dx

    return areal

trapes_sum = trapes_metode(a,b,n)
print(trapes_sum)




 