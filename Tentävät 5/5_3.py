from operator import truediv

luvut = [2,3,5,7]

luku = 99

while luku != 0:
    luku = int(input("Anna luku: "))

    kierros = 0

    for testiluku in luvut:

        if luku == testiluku:
            print("Alkuluku")
            break

        elif luku % testiluku == 0:
            print("Ei ole alkuluku")
            break

        elif kierros == 3:
            print("Alkuluku")
            break

        kierros += 1

