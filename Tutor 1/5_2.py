luku = 0
lista = []

while luku != "":
    luku = int(luku)
    lista.append(luku)

    luku = input("Anna luku: ")

    print(luku)

lista.sort(reverse=True)
print(lista)

for i in range(5):
    print(lista[i])

