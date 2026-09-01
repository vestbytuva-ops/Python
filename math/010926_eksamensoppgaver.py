# metode 1
# a = 100
# k = 9 / 10
# n = 8

# S_n = ((k**n - 1) / (k - 1)) * a

# print(S_n)

# metode 2
a = 100
k = 9 / 10
s = 0

for i in range(10):
    s = s + a
    print(i + 1, round(a), round(s))
    a = a * k
