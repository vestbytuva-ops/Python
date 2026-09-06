def f(x):
    return 0.06*x**2 + 4*x - 7

def snittfart (x1, x2):
    return (f(x2)-f(x1))/(x2-x1)
snitt = round(snittfart(-1,3),2)
print(f"Dette er den gjennomsnittlig momentanfarten til funksjonen {snitt}")
