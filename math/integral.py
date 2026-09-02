def f(x):
    return x**2+1

a=1
b=6
n=5
s=0

dx = (b - a)/n

for i in range(n):
    x = a + i*dx
    s = s + f(x)*dx

print(f"Areal {s}")