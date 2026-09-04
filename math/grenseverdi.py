def f(x):
    return 2*(x**2-16)/(x-4)
dx = 0.1
a=4
for i in range(5):
    x = a + dx
    print(x, " ", f(x))
    dx = dx*0.1