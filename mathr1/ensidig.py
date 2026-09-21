def f(x):
    return (x**2-4)/(x-2)

delta_x = 0.1
print("x, f(x)")

for i in range(3):
    x = 2 + delta_x
    y = round(f(x), 4)
    print(x, "," y)
    delta_x = delta_x / 10