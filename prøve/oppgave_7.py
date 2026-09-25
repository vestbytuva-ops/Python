from random import randint

l = [randint(1, 9) for _ in range(100)]


# Løsning med for-løkke
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


# Løsning med while-løkke
total = 0
antall = 0

while total <= 100 and antall < len(l):
    total += l[antall]
    antall += 1

if total > 100:
    print(f"While-løkke: {antall} tall gir summen {total}.")
else:
    print("While-løkke: Summen overstiger ikke 100.")
