command = input("Do we give more coins? ")

while command != "no":
    if command == "robbery":
        break
    print("Executing command: " + command)
    command = input("Do we give more coins? ")

print("That's enuff.")
