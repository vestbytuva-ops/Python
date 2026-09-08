def f(x):
    return 2*x**3

def snittfart (x1, x2):
    return (f(x2)-f(x1))/(x2-x1)

x0 = 3

snitt = round(snittfart(x0-1/2,x0+1/2),2)
print(f"Dette er den gjennomsnittlig momentanfarten til funksjonen {snitt}")
