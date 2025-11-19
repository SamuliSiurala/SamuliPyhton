nimet = set()

nimi = input("Anna nimi, tyhjä lopettaa: ")

while nimi != "":
    if nimet in nimi:
        print("Aiemmin syötetty nimi.")
        nimet.add(nimi)

    nimi = input("Anna nimi, tyhjä lopettaa: ")

print("Syötetyt nimet: ")
for n  in nimet:
    print(n)
