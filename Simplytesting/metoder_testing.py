text = "Tuvarakan er en svart DIGGER"

print(text.replace("D", "N"))   #Bytter ut D med N

text = text.replace("D", "N")

print(text.upper())             #Gjør alt til store bokstaver

print(text.lower())             #Gjør alt til små bokstaver

print(text.capitalize())        #Første bokstav blir stor, de andre blir små

print(text.title())             #Første bokstav i hver ord blir stor, resten bli små

print(text.index("G"))          #Finner indeks til første G. Starter å telle på null (blir 24)

print(text)                     #Skriver ut teksten "som den er"

# Lengde av en tekstreng
print(len(text))

a, b, c, d, e = text.split(' ') #deler strengen

print(a + c) #konkatenering
