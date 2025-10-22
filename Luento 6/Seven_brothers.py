def seven_brothers(lista):
    #järjestetään lista aakkosjärjestykseen
    lista.sort()

    #Tulostetaan nimet
    print(lista)
    return

#Pääohjelma
veljekset = ["Juhani", "Lauri", "Aapo", "Timo", "Tuomas", "Eero", "Simeoni"]
seven_brothers(veljekset)