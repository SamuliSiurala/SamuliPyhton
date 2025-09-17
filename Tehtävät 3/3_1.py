pituus = int(input("Anna kuhan pituus (cm): "))

alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Alamittainen, päästä takaisin. Puuttuu {puuttuu} cm")
else:
    print("Laillinen mitta.")
