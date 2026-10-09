class Planet:
    def __init__(self, navn, solavstand, radius, antallRinger = 0):
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
        self.antallRinger = antallRinger

planet1 = Planet("Merkur", 59.71, 2439.7, 0)
planet2 = Planet("Venus", 108.2, 6052, 0 )
planet3 = Planet("Mars", 227.9, 3359, 0 )

print(planet1.navn)
print(planet2.solavstand)
print(planet3.radius)