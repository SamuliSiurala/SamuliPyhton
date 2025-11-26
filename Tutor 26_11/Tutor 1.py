# for loop

lista = [0,9,2,3,5]

for i in lista:
    print(i)

# while loop

def luvut():
    luku = int(input("Anna luku: "))

    while luku > 0: # toista niin kauan kun luku on suurempi kuin 0
        print(luku)
        luku = int(input("Anna luku: "))

    return luku

# luvut()
luku = luvut()
print("Viimeinen luku oli", luku)