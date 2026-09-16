print("skriv in en streng")

tekst = input()
list = []

def mellomrom(tekst):
    return " " in tekst

if mellomrom(tekst):
    print("teksten inneholder mellomrom:")
    tekst = tekst.upper()
    list.append(tekst)
    print(list)

else:
    print("teksten inneholdr ikke mellomrom")
    tekst = tekst.upper()
    list.append(tekst)
    print(list)
