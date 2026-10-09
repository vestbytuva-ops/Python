saldo = 0
aar = 0

while saldo <= 60000:
    saldo += 1000
    saldo *= 1.06
    aar += 1

print(aar)
print(saldo)