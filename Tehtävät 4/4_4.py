import random

def arvauspeli():
    oikea = random.randint(1,10)
    print("Arvaa luku völiltä 1-10. Kirjoita 'q' lopettaaksesi")

    while True:
        s = input("Anna arvaus: ").strip()
        if s.lower() == 'q':
            print(f"Peli lopetettu, oikea luku on {oikea}.")
            break

        try:
            arv = int(s)
        except ValueError:
            print("Anna kokonaisluku tai valitse 'q' lopettaaksesi")
            continue

        if not (1 <= arv <= 10):
            print("Arvaus välille 1-10")
            continue

        if arv < oikea:
            print("Liian pieni")
        elif arv > oikea:
            print("Liian suuri")
        else:
            print("Oikein!")
            break

if __name__ == "__main__":
    arvauspeli()
