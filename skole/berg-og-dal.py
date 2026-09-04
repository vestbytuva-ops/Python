hoyde = int(input("Hvor høy er du?"))

if hoyde < 115:
    print(f"{hoyde}, Du er dessverre for liten og kan ikke kjøre")
elif hoyde >= 125:
    print(f"{hoyde}, Du er stor nok til å kjøre alene")
else:
    print(f"{hoyde}, Du må dessverre ha med en voksen")