LUOTI_GRAMMAA = 13.3
NAULA_LUOTIA = 32
LEIVISKA_NAULOJA = 20

leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))

kokonaisluodit = (leiviskat * LEIVISKA_NAULOJA * NAULA_LUOTIA +
                  naulat * NAULA_LUOTIA + luodit)

grammat = kokonaisluodit * LUOTI_GRAMMAA

kilogrammat = int(grammat // 1000)
grammat_jaljella = (grammat % 1000)

print(f"Massa on yhteensä {kilogrammat} kilogrammaa ja {grammat_jaljella:.2f} grammaa.")
