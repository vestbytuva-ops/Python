import math as m

syklist = 50
radius = 31.83
lengde = 100

banelengde = 2*radius*m.pi
fart = 50/3.6

print(f"Dette er avstanden rundt banen {banelengde}")
print(f"Dette er syklistens gjennomsnitt fart i {fart} m/s")
print(f"Dette er tiden syklisten bruker på 10 runder {10*banelengde/fart}")


