a=-2
b=0
n=8


def f(x):
    return x**3-4*x

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




