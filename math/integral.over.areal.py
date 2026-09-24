def f(x):
    return x**2 - 2*x + 2

a = 1
b = 5
n = 100

dx = (b - a) / n

# Venstresum
s = 0

for i in range(n):
    x = a + i * dx
# Høyresum
s = 0

for i in range(n):
    x = a + (i + 1) * dx
    s = s + f(x) * dx

print(f"Høyresum: {s}")