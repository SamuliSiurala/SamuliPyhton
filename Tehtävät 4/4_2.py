def tuumat_senttimetreiksi():
    while True:
        try:
            tuumat = float(input("Anna tuuma (negatiivinen lopettaa): "))
        except ValueError:
            print("Anna luku, ei tekstiä")
            continue

        if tuumat < 0:
            print("Lopetetaan")
            break
        else:
            cm = tuumat * 2.54
            print(f"(tuumat) tuumaa = {cm:.2f} cm")

tuumat_senttimetreiksi()

