def display_invoice(username, amout, due_data):
    print(f"hello {username}")
    print(f"hello bill of {amout:.2f} is due: {due_data}")

display_invoice("test", 100, "01/02")

#

def add(x,y):
    z = x + y
    return z


def substract(x,y):
    z = x - y
    return z

def multi(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z


print(add(1,2))
print(substract(1,2))
print(multi(1,2))
print(divide(1,2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)
#

def mail(navn, alder, by):
    navn = navn.lower()
    by = by.lower()
    return navn + alder + by + "@gmail.com"

mail_info = mail("test", "18" , "vestby")
print(mail_info)




def mail(navn, alder, sted):
    navn = navn.lower()
    sted = sted.lower()
    return navn + alder + sted + "@gmail.com"


navn = input("navn: ")
alder = input("alder: ")
sted = input("sted: ")

mail_info = mail(navn, alder, sted)

print(mail_info)

#

def fullt_navn(fornavn, etternavn):
    fornavn = fornavn.lower()
    etternavn = etternavn.lower()
    return fornavn + " " + etternavn

navn2 = fullt_navn("Ola", "Nordmann")

print(navn2)

#

def bruker_info2(navn2, alder2, by2):
    navn2 = navn2.lower()
    by2 = by2.lower()
    return navn2 + alder2 + by2

info2 = bruker_info2("test", "18", "vestby")

print(info2)

#
def lag_id(navn3, alder3):
    navn3 = navn3.lower()
    return navn3 + str(alder3)

info3 = lag_id("ola", 18)
print(info3)

#

def epost(navn, alder, sted):
    navn.lower()
    sted.lower()
    return navn + alder + sted + "@gmail.com"

