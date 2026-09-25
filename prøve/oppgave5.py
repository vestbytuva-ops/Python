def mail(navn, alder):
    navn = navn.lower()
    alder = str(alder)
    return navn + alder + "@pygame.pip"

input_navn = input("Navn: ")
input_alder = int(input("Alder: "))
print(mail(input_navn, input_alder))


#definerer funksjonen mail og gir paramterene navn og alder
#navn blir gjort om til små bokstaver fordi vi skal ikke ha noen store bokstaver i mailen
#alder blir gjort om til en streng fordi vi skal legge den sammen
#vi returnerer mailen 

#lager input for navn
#lager input for alder
#lager en mail ved å kalle på funksjonen mail og sender inn input navn og input alder som argumenter

