hours = {"Little Nightmares 1": 10, "Resident Evil 7 Biohazard": 109, "NieR: Automata": 90}

print("Going through your game history...")
print("Please wait...")
try:
    print(hours["Resident Evil 7 Biohazard"])
    print(hours["NieR: Automata"])
    print(hours["Elden Ring"])
    print(hours["Little Nightmares 1"])
except KeyError:
    print("Certain game not found")

print("Thank you!")