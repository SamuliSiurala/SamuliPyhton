import math

luku = int(input("Anna kokonaisluku (0 lopettaa): "))

while luku != 0:
    if luku < 0:
        print("Virheellinen numero")
    else:
        juuri = math.sqrt(luku)
        print("Neliöjuuri:", juuri)

    luku = int(input("Anna kokonaisluku (0 lopettaa): "))

print("Ohjelma päättyi.")