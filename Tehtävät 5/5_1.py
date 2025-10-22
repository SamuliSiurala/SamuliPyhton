import random

määrä = int(input("Anna kuutioiden määrä: "))
summa = 0

for i in range(määrä):
    heitto = random.randint(1,6)
    print("Heitto: ",heitto)
    summa += heitto
    print(summa)
