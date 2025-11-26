eläin = input("Mikä eläin?: ")

if eläin == "kissa" or eläin == "koira":
    print("Ok!")
    if eläin == "kissa":
        nimi = input("Mikä on kissan nimi? ")


elif eläin == "ihminen":
    print("Oho!")
    print("Monta ihmistä?")

else:
    print("Voi ei!")

print("Eläin oli " + eläin + " ja sen nimi oli " + nimi)
