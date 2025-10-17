from operator import truediv

luvut = [2,3,5,7]

while True:
    luku = int(input("Anna luku: "))

    for testiluku in luvut:

        if luku % testiluku == 0:
            print("Ei ole alkuluku")
            break

