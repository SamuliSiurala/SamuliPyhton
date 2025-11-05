import math

def yksikköhinta(halkaisija, hinta):
    "lasketaan pizzan pinta-ala neliömetreinä
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade / 100) **2 #cm -> metreiksi
    #Yksikköhinta = €/nm2
    return hinta / pinta_ala

#Main program
halkaisija1 = float(input("Halkaisija pizza1 (cm): "))
hinta1 = float(input("Hinta pizza1 (€): "))

halkaisija2 = float(input("Halkaisija pizza2 (cm): "))
hinta2 = float(input("Hinta pizza2 (€): "))

#Lasketaan yksikköhinnat
pizza1 = yksikköhinta(halkaisija1, hinta1))
pizza2 = yksikköhinta(halkaisija2, hinta2))
print(f'Pizza 1 yksikköhinta on {pizza1: 2f} €/nm2*)