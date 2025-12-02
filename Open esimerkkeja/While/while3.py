tarina = ""
#edellinen = ""  
sana = input("Anna sana lisättäväksi tarinaan: ")

while sana != "loppu": #and sana != edellinen:
    if tarina == "":
        tarina = sana
    else:
        tarina = tarina + " " + sana

    #edellinen = sana
    sana = input("Anna sana lisättäväksi tarinaan: ")

print(tarina)


#Kommenttina bonus-osio