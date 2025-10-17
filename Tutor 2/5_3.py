from operator import truediv

luvut = [2,3,5,7]

while True:
    luku = int(input("Anna luku: "))

    for i in range(3):

        if luku % luvut[i] == 0:
            print("Ei ole alkuluku")
            break
        elif luvut[i] == 5:
            print("Alkuluku")

