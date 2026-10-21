
from math import isclose

a = float(input("Skriv inn a: "))
b = float(input("Skriv inn b: "))
c = float(input("Skriv inn c: "))
d = float(input("Skriv inn d: "))

x = float(input("Skriv inn x-koordinaten: "))
y = float(input("Skriv inn y-koordinaten: "))

if b != 0:
    t = (x - a) / b
    ligger_paa = isclose(y, c + d*t)
elif d != 0:
    t = (y - c) / d
    ligger_paa = isclose(x, a + b*t)
else:
    ligger_paa = isclose(x, a) and isclose(y, c)

if ligger_paa:
    print("Punktet ligger på linja")
else:
    print("Punktet ligger ikke på linja")
