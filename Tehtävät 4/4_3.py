def main():
    luvut = []

    while True:
        syote = input("Anna luku, tai lopeta Enerillä): ")
        if syote == "":
            break

        try:
            luku = float(syote)
            luvut.append(luku)
        except ValueError:
            print("Virheellinen, anna luku")

    if luvut:
        print("Pienin luku:", min(luvut))
        print("Suurin luku:", max(luvut))
    else:
        print("Et antanut lukua")

if __name__ == "__main__":
    main()