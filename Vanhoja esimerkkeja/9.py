#Järjestys tärkeä!

luku = int(input("Anna kokonaisluku: "))

if luku % 3 == 0 and luku % 5 == 0:
    print("BOOMBuzz")
elif luku % 3 == 0:
    print("BOOM")
elif luku % 5 == 0:
    print("Buzz")

