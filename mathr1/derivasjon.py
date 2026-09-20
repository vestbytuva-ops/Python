def f(x):
    return (3* x+1)/(x-2)

def snittfart(a):
    return(f(a+dx)-f(a))/dx

dx = 0.1
a = -4

for i in range(4):
    print(snittfart(a))
    dx = dx*0.1