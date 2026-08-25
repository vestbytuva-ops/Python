# a = 1
# s = 0
# for i in range(10):
#     s = s + a
#     print(a, s)
#     a = a + 2

# a = 1
# s = 0
# n = 1
# for i in range(50):
#     s = s + a
#     print(a, s)
#     n = n + 1
#     a = 2*n-1


# s = 0
# n = 1
# f = n**2 - 2
# for i in range(50):
#     s = s + f
#     print(f, s)
#     n = n + 1
#     f = n**2 - 2

# s = 0
# n = 1
# b = 3*2**n
# for i in range(50):
#     s = s + b
#     print(b, s)
#     n = n + 1
#     b = 3*2**n

# s = 0
# n = 1
# g = 50*0.89**(n-1)
# for i in range(50):
#     s = s + g
#     print(g, s)
#     n = n + 1
#     g = 50*0.89**(n-1)

s = 0
N = 10
a_1 = 3
a_n = 69
d = 6
n = a_1 + (N - 1) * d
S_n = ((a_1 + a_n)/2)*n

print(S_n)
