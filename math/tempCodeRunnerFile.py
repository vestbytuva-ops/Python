s = 0
n = 1
b = 3*2**n
for i in range(50):
    s = s + b
    print(b, s)
    n = n + 1
    b = 3*2**n