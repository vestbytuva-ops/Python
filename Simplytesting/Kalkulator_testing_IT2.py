#svar oppgave 10
def main():
    valg = str(input("Liter til desiliter (tast inn a), " "Fahrenheit til celsius (tast inn b), " "Minutter til timer (tast inn c), " "slutt (tast inn x)"))
    
    if valg == "a":
        liquid()

    elif valg == "b":
        temperature()
        
    elif valg == "c":
        time()
    
    elif valg == "x":
        return
    
    main()
    return

def liquid():                                                       # konverterer liter til desiliter
    tall = float(input("Tast inn antall liter:"))
    return (print(tall*10, "dl"))

def temperature():                                                  # konverterer fahrenheit til celsius
    tall = float(input("Tast inn antall grader fahrenheit:"))
    return (print((tall - 32) * 5 / 9, "C°"))

def time():                                                         # konverterer minutter til timer
    tall = float(input("Tast inn antall minutter:"))
    return (print(tall // 60, "t", tall % 60, "min"))

main()
