viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai",
"perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän \n"
                "järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print(f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")

