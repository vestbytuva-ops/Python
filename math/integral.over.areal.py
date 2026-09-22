def f(x):
    return x**2-2*x+2

a=1
b=5
n=100
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