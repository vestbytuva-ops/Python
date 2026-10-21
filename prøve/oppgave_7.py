#kodee under brukes til å genere en liste med 100 tilfeldige tall mellom 1 og 9
#lag et program som legger sammen tallene i listen (fra venstre mot høyre) og finner ut hvor mang e tall den må summere før summe n overstiger 100. Løs oppgaven både med en for og while løkke.


from random import randint
l = [randint(1,9) for _ in range(100)]

while sum < 100:
    sum = 0
    for i in l:
        sum += i
print(sum)

# løsning med for-løkke
total = 0
antall = 0

for tall in l:
    total += tall
    antall += 1

    if total > 100:
        print(f"For-løkke: {antall} tall gir summen {total}.")
        break
else:
    print("For-løkke: Summen overstiger ikke 100.")

for i in range(1,9):
    print(i)


# løsning med while-løkke
total = 0
antall = 0

while total <= 100 and antall < len(l):
    total += l[antall]
    antall += 1

if total > 100:
    print(f"While-løkke: {antall} tall gir summen {total}.")
else:
    print("While-løkke: Summen overstiger ikke 100.")