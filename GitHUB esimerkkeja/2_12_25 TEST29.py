numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numerot["Olga"] = "050-1010101"
numerot["Mary"] = "0401+2121212"

print(numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print(f"Henkilön {nimi} numero on {numerot[nimi]}.")

