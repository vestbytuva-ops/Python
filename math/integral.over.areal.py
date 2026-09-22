def f(x):
    return -x**2-x+20

a=0
b=4
n=10000
s=0

dx = (b - a)/n

for i in range(n):
    x = a + i *dx
    s = s + f(x)*dx

print(f"Areal {s}")

for i in range(n):
    x = a + (i+1) *dx
    s = s + f(x)*dx

print(f"Areal {s}")